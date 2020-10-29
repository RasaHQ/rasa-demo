# -*- coding: utf-8 -*-
import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

from actions import config
from actions.api import community_events
from actions.api.algolia import AlgoliaAPI
from actions.api.discourse import DiscourseAPI
from actions.api.gdrive_service import GDriveService
from actions.api.mailchimp import MailChimpAPI

logger = logging.getLogger(__name__)

INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_description_mapping.csv"


class ActionSubmitSubscribeNewsletterForm(Action):
    def name(self) -> Text:
        return "action_submit_subscribe_newsletter_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have an email, attempt to add it to the database"""

        email = tracker.get_slot("email")
        client = MailChimpAPI(config.mailchimp_api_key)
        # if the email is already subscribed, this returns False
        added_to_list = client.subscribe_user(config.mailchimp_list, email)

        # utter submit template
        if added_to_list:
            dispatcher.utter_message(template="utter_confirmationemail")
        else:
            dispatcher.utter_message(template="utter_already_subscribed")
        return []


class ValidateSubscribeNewsletterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_subscribe_newsletter_form"

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if MailChimpAPI.is_valid_email(value):
            return {"email": value}
        else:
            dispatcher.utter_message(template="utter_no_email")
            return {"email": None}


class ActionSubmitSalesForm(Action):
    def name(self) -> Text:
        return "action_submit_sales_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""

        import datetime

        budget = tracker.get_slot("budget")
        company = tracker.get_slot("company")
        email = tracker.get_slot("business_email")
        job_function = tracker.get_slot("job_function")
        person_name = tracker.get_slot("person_name")
        use_case = tracker.get_slot("use_case")
        date = datetime.datetime.now().strftime("%d/%m/%Y")

        sales_info = [company, use_case, budget, date, person_name, job_function, email]

        try:
            gdrive = GDriveService()
            gdrive.store_data(sales_info)
            dispatcher.utter_message(template="utter_confirm_salesrequest")
            return []
        except Exception as e:
            logger.error(
                "Failed to write data to gdocs. Error: {}" "".format(e.message),
                exc_info=True,
            )
            dispatcher.utter_message(template="utter_salesrequest_failed")
            return []


class ValidateSalesForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_sales_form"

    def validate_business_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if MailChimpAPI.is_valid_email(value):
            return {"business_email": value}
        else:
            dispatcher.utter_message(template="utter_no_email")
            return {"business_email": None}


class ActionExplainSalesForm(Action):
    """Returns the explanation for the sales form questions"""

    def name(self) -> Text:
        return "action_explain_sales_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        requested_slot = tracker.get_slot("requested_slot")

        sales_form_config = domain.get("forms", {}).get("sales_form", {})
        sales_form_required_slots = list(sales_form_config.keys())

        if requested_slot not in sales_form_required_slots:
            dispatcher.utter_message(
                template="Sorry, I didn't get that. Please rephrase or answer the question "
                "above."
            )
            return []

        dispatcher.utter_message(template=f"utter_explain_{requested_slot}")
        return []


class ActionExplainFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_explain_faq"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        topic = tracker.get_slot("faq")

        if topic in ["channels", "languages", "ee", "slots", "voice"]:
            dispatcher.utter_message(template=f"utter_faq_{topic}_more")
        else:
            dispatcher.utter_message(template="utter_no_further_info")

        return []


class ActionSetFaqSlot(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_set_faq_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        full_intent = (
            tracker.latest_message.get("response_selector", {})
            .get("faq", {})
            .get("full_retrieval_intent")
        )
        if full_intent:
            topic = full_intent.split("/")[1]
        else:
            topic = None

        return [SlotSet("faq", topic)]


class ActionPause(Action):
    """Pause the conversation"""

    def name(self) -> Text:
        return "action_pause"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        return [ConversationPaused()]


class ActionStoreUnknownProduct(Action):
    """Stores unknown tools people are migrating from in a slot"""

    def name(self) -> Text:
        return "action_store_unknown_product"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        # if we dont know the product the user is migrating from,
        # store their last message in a slot.
        return [SlotSet("unknown_product", tracker.latest_message.get("text"))]


class ActionStoreUnknownNluPart(Action):
    """Stores unknown parts of nlu which the user requests information on
    in slot.
    """

    def name(self) -> Text:
        return "action_store_unknown_nlu_part"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        # if we dont know the part of nlu the user wants information on,
        # store their last message in a slot.
        return [SlotSet("unknown_nlu_part", tracker.latest_message.get("text"))]


class ActionStoreBotLanguage(Action):
    """Takes the bot language and checks what pipelines can be used"""

    def name(self) -> Text:
        return "action_store_bot_language"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        spacy_languages = [
            "english",
            "french",
            "german",
            "spanish",
            "portuguese",
            "french",
            "italian",
            "dutch",
        ]
        language = tracker.get_slot("language")
        if not language:
            return [
                SlotSet("language", "that language"),
                SlotSet("can_use_spacy", False),
            ]

        if language.lower() in spacy_languages:
            return [SlotSet("can_use_spacy", True)]
        else:
            return [SlotSet("can_use_spacy", False)]


class ActionStoreEntityExtractor(Action):
    """Takes the entity which the user wants to extract and checks
    what pipelines can be used.
    """

    def name(self) -> Text:
        return "action_store_entity_extractor"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        spacy_entities = ["place", "date", "name", "organisation"]
        duckling = [
            "money",
            "duration",
            "distance",
            "ordinals",
            "time",
            "amount-of-money",
            "numbers",
        ]

        entity_to_extract = next(tracker.get_latest_entity_values("entity"), None)

        extractor = "CRFEntityExtractor"
        if entity_to_extract in spacy_entities:
            extractor = "SpacyEntityExtractor"
        elif entity_to_extract in duckling:
            extractor = "DucklingHTTPExtractor"

        return [SlotSet("entity_extractor", extractor)]


class ActionSetOnboarding(Action):
    """Sets the slot 'onboarding' to true/false dependent on whether the user
    has built a bot with rasa before"""

    def name(self) -> Text:
        return "action_set_onboarding"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        user_type = next(tracker.get_latest_entity_values("user_type"), None)
        is_new_user = intent == "how_to_get_started" and user_type == "new"
        if intent == "affirm" or is_new_user:
            return [SlotSet("onboarding", True)]
        elif intent == "deny":
            return [SlotSet("onboarding", False)]
        return []


class ActionSubmitSuggestionForm(Action):
    def name(self) -> Text:
        return "action_submit_suggestion_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        dispatcher.utter_message(template="utter_thank_suggestion")
        return []


class ActionStoreProblemDescription(Action):
    """Stores the problem description in a slot."""

    def name(self) -> Text:
        return "action_store_problem_description"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        problem = tracker.latest_message.get("text")

        return [SlotSet("problem_description", problem)]


class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        shown_privacy = tracker.get_slot("shown_privacy")
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        if intent == "next_step":
            intent = "get_started_step1"
        if intent == "greet" or (intent == "enter_data" and name_entity):
            if shown_privacy and name_entity and name_entity.lower() != "sara":
                dispatcher.utter_message(template="utter_greet_name", name=name_entity)
                return []
            elif shown_privacy:
                dispatcher.utter_message(template="utter_greet_noname")
                return []
            else:
                dispatcher.utter_message(template="utter_greet")
                dispatcher.utter_message(template="utter_inform_privacypolicy")
                dispatcher.utter_message(template="utter_ask_goal")
                return [SlotSet("shown_privacy", True)]
        elif intent[:-1] == "get_started_step" and not shown_privacy:
            dispatcher.utter_message(template="utter_greet")
            dispatcher.utter_message(template="utter_inform_privacypolicy")
            dispatcher.utter_message(template=f"utter_{intent}")
            return [SlotSet("shown_privacy", True), SlotSet("step", intent[-1])]
        elif intent[:-1] == "get_started_step" and shown_privacy:
            dispatcher.utter_message(template=f"utter_{intent}")
            return [SlotSet("step", intent[-1])]
        return []


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]

        # for the intent name used to retrieve the button title, we either use
        # the name of the name of the "main" intent, or if it's an intent that triggers
        # the response selector, we use the full retrieval intent name so that we
        # can distinguish between the different sub intents
        first_intent_names = [
            intent.get("name", "")
            if intent.get("name", "") not in ["out_of_scope", "faq", "chitchat"]
            else tracker.latest_message.get("response_selector")
            .get(intent.get("name", ""))
            .get("full_retrieval_intent")
            for intent in intent_ranking
        ]
        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            button_title = self.get_button_title(intent, entities)
            if "/" in intent:
                # here we use the button title as the payload as well, because you
                # can't force a response selector sub intent, so we need NLU to parse
                # that correctly
                buttons.append({"title": button_title, "payload": button_title})
            else:
                buttons.append(
                    {"title": button_title, "payload": f"/{intent}{entities_json}"}
                )

        buttons.append({"title": "Something else", "payload": "/out_of_scope"})

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_message(template="utter_restart_with_button")

            return [SlotSet("feedback_value", "negative"), ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_default")
            return [UserUtteranceReverted()]


class CommunityEventAction(Action):
    """Utters Rasa community events."""

    def __init__(self) -> None:
        self.last_event_update = None
        self.events = None
        self.events = self._get_events()

    def name(self) -> Text:
        return "action_get_community_events"

    def _get_events(self) -> List[community_events.CommunityEvent]:
        if self.events is None or self._are_events_expired():
            logger.debug("Getting events from website.")
            self.last_event_update = datetime.now()
            self.events = community_events.get_community_events()

        return self.events

    def _are_events_expired(self) -> bool:
        # events are expired after 1 hour
        return (
            self.last_event_update is None
            or (datetime.now() - self.last_event_update).total_seconds() > 3600
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        events = self._get_events()
        location = next(tracker.get_latest_entity_values("location"), None)
        events_for_location = None
        if location:
            location = location.title()
            events_for_location = [
                e
                for e in events
                if e.city.lower() == location.lower()
                or e.country.lower() == location.lower()
            ]

        if not events:
            dispatcher.utter_message(
                text="Looks like we don't have currently have any Rasa events planned."
            )
        else:
            self._utter_events(
                tracker, dispatcher, events, events_for_location, location
            )

        return []

    @staticmethod
    def _utter_events(
        tracker: Tracker,
        dispatcher: CollectingDispatcher,
        events: List,
        events_for_location: List,
        location: Text,
    ) -> None:

        only_next = True if "next" in tracker.latest_message.get("text") else False

        if location:
            if not events_for_location:
                header = (
                    f"Sorry, there are currently no events in {location}. \n\n"
                    "However, here are the upcoming Rasa events:"
                )
                if only_next:
                    header = (
                        f"Sorry, there are currently no events in {location}. \n\n"
                        "However, here is the next Rasa event:"
                    )

            else:
                events = events_for_location
                header = f"Here are the upcoming Rasa events in {location}:"
                if only_next:
                    header = f"Here is the next event in {location}:"

        else:
            header = "Here are the upcoming Rasa events:"
            if only_next:
                header = "Here is the next Rasa event:"

        if only_next:
            events = events[0:1]

        event_items = [f"- {e.name_as_link()} in {e.city}" for e in events]
        events = "\n".join(event_items)
        dispatcher.utter_message(
            text=f"{header} \n\n {events} \n\n We hope to see you there!"
        )


class ActionNextStep(Action):
    def name(self) -> Text:
        return "action_next_step"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        if tracker.get_slot("step"):
            step = int(tracker.get_slot("step")) + 1

            if step in [2, 3, 4]:
                dispatcher.utter_message(template=f"utter_continue_step{step}")
            else:
                dispatcher.utter_message(template="utter_no_more_steps")

            return []

        else:
            return [FollowupAction("action_greet_user")]


def get_last_event_for(tracker, event_type: Text, skip: int = 0) -> Optional[EventType]:
    skipped = 0
    for e in reversed(tracker.events):
        if e.get("event") == event_type:
            skipped += 1
            if skipped > skip:
                return e
    return None


class ActionDocsSearch(Action):
    def name(self):
        return "action_docs_search"

    def run(self, dispatcher, tracker, domain):
        docs_found = False
        search_text = tracker.latest_message.get("text")

        # Search of docs pages
        algolia_result = None
        algolia = AlgoliaAPI(
            config.algolia_app_id, config.algolia_search_key, config.algolia_docs_index
        )
        if search_text == "/technical_question{}":
            # If we're in a TwoStageFallback we need to look back one more user utterance
            # to get the actual text
            last_user_event = get_last_event_for(tracker, "user", skip=2)
            if last_user_event:
                search_text = last_user_event.get("text")
                algolia_result = algolia.search(search_text)
        else:
            algolia_result = algolia.search(search_text)

        if (
            algolia_result
            and algolia_result.get("hits")
            and len(algolia_result.get("hits")) > 0
        ):
            docs_found = True
            hits = [
                hit
                for hit in algolia_result.get("hits")
                if "Rasa X Changelog " not in hit.get("hierarchy", {}).values()
                and "Rasa Open Source Change Log "
                not in hit.get("hierarchy", {}).values()
            ]
            if not hits:
                hits = algolia_result.get("hits")
            doc_list = algolia.get_algolia_link(hits, 0)
            doc_list += (
                "\n" + algolia.get_algolia_link(hits, 1)
                if len(algolia_result.get("hits")) > 1
                else ""
            )

            dispatcher.utter_message(
                text="I can't answer your question directly, but I found the following from the docs:\n"
                + doc_list
            )

        else:
            dispatcher.utter_message(
                text=(
                    "I can't answer your question directly, and also "
                    "found nothing in our documentation that would help."
                )
            )

        return [SlotSet("docs_found", docs_found)]


class ActionForumSearch(Action):
    def name(self):
        return "action_forum_search"

    def run(self, dispatcher, tracker, domain):
        search_text = tracker.latest_message.get("text")
        # If we're in a TwoStageFallback we need to look back two more user utterance to get the actual text
        if search_text == "/technical_question{}" or search_text == "/deny":
            last_user_event = get_last_event_for(tracker, "user", skip=3)
            if last_user_event:
                search_text = last_user_event.get("text")
            else:
                dispatcher.utter_message(text="Sorry, I can't answer your question.")
                return []

        # Search forum
        discourse = DiscourseAPI("https://forum.rasa.com/search")
        disc_res = discourse.query(search_text)
        disc_res = disc_res.json()

        if disc_res and disc_res.get("topics") and len(disc_res.get("topics")) > 0:
            forum = discourse.get_discourse_links(disc_res.get("topics"), 0)
            forum += (
                "\n" + discourse.get_discourse_links(disc_res.get("topics"), 1)
                if len(disc_res.get("topics")) > 1
                else ""
            )

            dispatcher.utter_message(
                text=f"I found the following from our forum:\n{forum}"
            )
        else:
            dispatcher.utter_message(
                text=(
                    "I did not find any matching issues on our [forum](https://forum.rasa.com/):\n"
                    "I recommend you post your question there."
                )
            )

        return []


def tag_convo(tracker: Tracker, label: Text) -> None:
    """Tag a conversation in Rasa X with a given label"""
    endpoint = f"http://{config.rasa_x_host}/api/conversations/{tracker.sender_id}/tags"
    requests.post(url=endpoint, data=label)
    return


class ActionTagFeedback(Action):
    """Tag a conversation in Rasa X as positive or negative feedback """

    def name(self):
        return "action_tag_feedback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        feedback = tracker.get_slot("feedback_value")

        if feedback == "positive":
            label = '[{"value":"postive feedback","color":"76af3d"}]'
        elif feedback == "negative":
            label = '[{"value":"negative feedback","color":"ff0000"}]'
        else:
            return []

        tag_convo(tracker, label)

        return []


class ActionTagDocsSearch(Action):
    """Tag a conversation in Rasa X according to whether the docs search was helpful"""

    def name(self):
        return "action_tag_docs_search"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")

        if intent == "affirm":
            label = '[{"value":"docs search helpful","color":"e5ff00"}]'
        elif intent == "deny":
            label = '[{"value":"docs search unhelpful","color":"eb8f34"}]'
        else:
            return []

        tag_convo(tracker, label)

        return []
