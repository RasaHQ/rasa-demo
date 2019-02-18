# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from typing import Text, Dict, Any, List
import json

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
    ConversationPaused, FollowupAction, Form

from demo.api import MailChimpAPI
from demo import config
from demo.gdrive_service import GDriveService

logger = logging.getLogger(__name__)


class ActionSubscribeNewsletter(Action):
    """ This action calls our newsletter API and subscribes the user with
    their email address"""

    def name(self):
        return "action_subscribe_newsletter"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email')
        if email:
            client = MailChimpAPI(config.mailchimp_api_key)
            # if the email is already subscribed, this returns False
            subscribed = client.subscribe_user(config.mailchimp_list, email)

            return [SlotSet('subscribed', subscribed)]
        return []


class ActionStoreSalesInfo(Action):
    """Saves the information collected in the sales flow into a spreadsheet"""

    def name(self):
        return "action_store_sales_info"

    def run(self, dispatcher, tracker, domain):
        import datetime
        budget = tracker.get_slot('budget')
        company = tracker.get_slot('company_name')
        email = tracker.get_slot('email')
        jobfunction = tracker.get_slot('job_function')
        name = tracker.get_slot('person_name')
        use_case = tracker.get_slot('use_case')
        date = datetime.datetime.now().strftime("%d/%m/%Y")

        sales_info = [company, use_case, budget, date, name, jobfunction,
                      email]

        gdrive = GDriveService()
        try:
            gdrive.store_data(sales_info)
            return [SlotSet('data_stored', True)]
        except Exception as e:
            logger.error("Failed to write data to gdocs. Error: {}"
                         "".format(e.message), exc_info=True)
            return [SlotSet('data_stored', False)]


class ActionStoreBudget(Action):
    """Stores the budget in a slot"""

    def name(self):
        return "action_store_budget"

    def run(self, dispatcher, tracker, domain):

        # the entity can be one of two entities from duckling,
        # number or amount-of-money
        budget = next(tracker.get_latest_entity_values('number'), None)
        if not budget:
            budget = next(tracker.get_latest_entity_values('amount-of-money'),
                          None)

        # as a fallback, if no entity is recognised (e.g. in a sentence
        # like "I have no money") we store the whole user utterance in the slot
        # In future this should be stored in a `budget_unconfirmed` slot where
        # the user will then be asked to confirm this is there budget
        if not budget:
            budget = tracker.latest_message.get('text')

        return [SlotSet('budget', budget)]


class ActionStoreUsecase(Action):
    """Stores the bot use case in a slot"""

    def name(self):
        return "action_store_usecase"

    def run(self, dispatcher, tracker, domain):
        # we grab the whole user utterance here as there are no real entities
        # in the use case
        use_case = tracker.latest_message.get('text')

        return [SlotSet('use_case', use_case)]


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_builder', 'ask_weather', 'ask_howdoing',
                      'ask_whatspossible', 'ask_whatisrasa', 'ask_isbot',
                      'ask_howold', 'ask_languagesbot', 'ask_restaurant',
                      'ask_time', 'ask_wherefrom', 'ask_whoami',
                      'handleinsult', 'nicetomeeyou', 'telljoke',
                      'ask_whatismyname', 'howwereyoubuilt', 'ask_whoisit']:
            dispatcher.utter_template('utter_' + intent, tracker)
        return []


class ActionFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_faqs"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_faq_platform', 'ask_faq_languages',
                      'ask_faq_tutorialcore', 'ask_faq_tutorialnlu',
                      'ask_faq_opensource', 'ask_faq_voice', 'ask_faq_slots',
                      'ask_faq_channels', 'ask_faq_differencecorenlu',
                      'ask_faq_python_version', 'ask_faq_community_size',
                      'ask_faq_what_is_forum', 'ask_faq_tutorials']:
            dispatcher.utter_template('utter_' + intent, tracker)
        return []


class ActionStoreName(Action):
    """Stores the users name in a slot"""

    def name(self):
        return "action_store_name"

    def run(self, dispatcher, tracker, domain):
        person_name = next(tracker.get_latest_entity_values('name'), None)

        # if no name was extracted, use the whole user utterance
        # in future this will be stored in a `name_unconfirmed` slot and the
        # user will be asked to confirm their name
        if not person_name:
            person_name = tracker.latest_message.get('text')

        return [SlotSet('person_name', person_name)]


class ActionStoreCompany(Action):
    """Stores the company name in a slot"""

    def name(self):
        return "action_store_company"

    def run(self, dispatcher, tracker, domain):
        company = next(tracker.get_latest_entity_values('company'), None)

        # if no company entity was extracted, use the whole user utterance
        # in future this will be stored in a `company_unconfirmed` slot and
        # the user will be asked to confirm their company name
        if not company:
            company = tracker.latest_message.get('text')

        return [SlotSet('company_name', company)]


class ActionStoreJob(Action):
    """Stores the job in a slot"""

    def name(self):
        return "action_store_job"

    def run(self, dispatcher, tracker, domain):
        jobfunction = next(tracker.get_latest_entity_values('jobfunction'),
                           None)

        # if no jobfunction entity was extracted, use the whole user utterance
        # in future this will be stored in a `job_unconfirmed` slot and
        # the user will be asked to confirm their job title
        if not jobfunction:
            jobfunction = tracker.latest_message.get('text')

        return [SlotSet('job_function', jobfunction)]


class ActionStoreEmail(Action):
    """Stores the email in a slot"""

    def name(self):
        return "action_store_email"

    def run(self, dispatcher, tracker, domain):
        email = next(tracker.get_latest_entity_values('email'), None)

        # if no email entity was recognised, prompt the user to enter a valid
        # email and go back a turn in the conversation to ensure future
        # predictions aren't affected
        if not email:
            dispatcher.utter_message("We need your email, "
                                     "please enter a valid one.")
            return [UserUtteranceReverted()]

        return [SlotSet('email', email)]


class ActionPause(Action):
    """Pause the conversation"""

    def name(self):
        return "action_pause"

    def run(self, dispatcher, tracker, domain):
        return [ConversationPaused()]


class ActionStoreUnknownProduct(Action):
    """Stores unknown tools people are migrating from in a slot"""

    def name(self):
        return "action_store_unknown_product"

    def run(self, dispatcher, tracker, domain):
        # if we dont know the product the user is migrating from,
        # store his last message in a slot.
        return [SlotSet('unknown_product', tracker.latest_message.get('text'))]


class ActionStoreUnknownNluPart(Action):
    """Stores unknown parts of nlu which the user requests information on
       in slot.
    """

    def name(self):
        return "action_store_unknown_nlu_part"

    def run(self, dispatcher, tracker, domain):
        # if we dont know the part of nlu the user wants information on,
        # store his last message in a slot.
        return [SlotSet('unknown_nlu_part',
                tracker.latest_message.get('text'))]


class ActionStoreBotLanguage(Action):
    """Takes the bot language and checks what pipelines can be used"""

    def name(self):
        return "action_store_bot_language"

    def run(self, dispatcher, tracker, domain):
        spacy_languages = ['english', 'french', 'german', 'spanish',
                           'portuguese', 'french', 'italian', 'dutch']
        language = tracker.get_slot('language')
        if not language:
            return [SlotSet('language', 'that language'),
                    SlotSet('can_use_spacy', False)]

        if language in spacy_languages:
            return [SlotSet('can_use_spacy', True)]
        else:
            return [SlotSet('can_use_spacy', False)]


class ActionStoreEntityExtractor(Action):
    """Takes the entity which the user wants to extract and checks
        what pipelines can be used.
    """

    def name(self):
        return "action_store_entity_extractor"

    def run(self, dispatcher, tracker, domain):
        spacy_entities = ['place', 'date', 'name', 'organisation']
        duckling = ['money', 'duration', 'distance', 'ordinals', 'time',
                    'amount-of-money', 'numbers']

        entity_to_extract = next(tracker.get_latest_entity_values('entity'),
                                 None)

        extractor = 'ner_crf'
        if entity_to_extract in spacy_entities:
            extractor = 'ner_spacy'
        elif entity_to_extract in duckling:
            extractor = 'ner_duckling_http'

        return [SlotSet('entity_extractor', extractor)]


class ActionSetOnboarding(Action):
    """Sets the slot 'onboarding' to true/false dependent on whether the user
    has built a bot with rasa before"""

    def name(self):
        return "action_set_onboarding"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        user_type = next(tracker.get_latest_entity_values("user_type"), None)
        is_new_user = intent == "how_to_get_started" and user_type == "new"
        if intent == 'affirm' or is_new_user:
            return [SlotSet('onboarding', True)]
        elif intent == 'deny':
            return [SlotSet('onboarding', False)]
        return []


class SuggestionForm(FormAction):
    """Accept free text input from the user for suggestions"""

    def name(self):
        return "suggestion_form"

    @staticmethod
    def required_slots(tracker):
        return ["suggestion"]

    def slot_mappings(self):
        return {"suggestion": self.from_text()}

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_thank_suggestion', tracker)
        return []


class ActionStackInstallationCommand(Action):
    """Utters the installation command for rasa depending whether
       they are using `pip` or `conda`
    """

    def name(self):
        return "action_select_installation_command"

    def run(self, dispatcher, tracker, domain):
        package_manager = tracker.get_slot('package_manager')

        if package_manager == 'conda':
            dispatcher.utter_template('utter_installation_with_conda', tracker)
        else:
            dispatcher.utter_template('utter_installation_with_pip', tracker)

        return []


class ActionStoreProblemDescription(Action):
    """Stores the problem description in a slot."""

    def name(self):
        return "action_store_problem_description"

    def run(self, dispatcher, tracker, domain):
        problem = tracker.latest_message.get('text')

        return [SlotSet('problem_description', problem)]


class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self):
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        shown_privacy = tracker.get_slot("shown_privacy")
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        if intent == "greet":
            if shown_privacy and name_entity and name_entity.lower() != 'sara':
                dispatcher.utter_template("utter_greet_name", tracker,
                                          name=name_entity)
                return []
            elif shown_privacy:
                dispatcher.utter_template("utter_greet_noname", tracker)
                return []
            else:
                dispatcher.utter_template("utter_greet", tracker)
                dispatcher.utter_template("utter_inform_privacypolicy", tracker)
                dispatcher.utter_template("utter_ask_goal", tracker)
                return [SlotSet('shown_privacy', True)]
        elif intent[:-1] == 'get_started_step' and not shown_privacy:
            dispatcher.utter_template("utter_greet", tracker)
            dispatcher.utter_template("utter_inform_privacypolicy", tracker)
            dispatcher.utter_template("utter_"+intent, tracker)
            return [SlotSet('shown_privacy', True), SlotSet('step', intent[-1])]
        elif intent[:-1] == 'get_started_step' and shown_privacy:
            dispatcher.utter_template("utter_"+intent, tracker)
            return [SlotSet('step', intent[-1])]
        return []


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv("data/"
                                           "intent_description_mapping.csv")
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(',')})

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List['Event']:

        intent_ranking = tracker.latest_message.get('intent_ranking', [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = (intent_ranking[0].get("confidence") -
                                      intent_ranking[1].get("confidence"))
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        first_intent_names = [intent.get('name', '')
                              for intent in intent_ranking
                              if intent.get('name', '') != 'out_of_scope']

        message_title = ("Sorry, I'm not sure I've understood "
                         "you correctly 🤔 Do you mean...")

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            logger.debug(intent)
            logger.debug(entities)
            buttons.append({'title': self.get_button_title(intent, entities),
                            'payload': '/{}{}'.format(intent,
                                                      entities_json)})

        buttons.append({'title': 'Something else',
                        'payload': '/out_of_scope'})

        dispatcher.utter_button_message(message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]
                         ) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (
                (self.intent_mappings.entities == entities.keys()) &
                default_utterance_query)

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = (
                self.intent_mappings[default_utterance_query]
                    .button.tolist())
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List['Event']:

        # Fallback caused by TwoStageFallbackPolicy
        if (len(tracker.events) >= 4 and
                tracker.events[-4].get('name') ==
                'action_default_ask_affirmation'):

            dispatcher.utter_template('utter_restart_with_button', tracker)

            return [SlotSet('feedback_value', 'negative'),
                    ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_template('utter_default', tracker)
            return [UserUtteranceReverted()]


class CommunityEventAction(Action):
    """Utters Rasa community events."""

    def __init__(self):
        self.last_event_update = None
        self.events = None
        self.events = self._get_events()

    def name(self) -> Text:
        return "action_get_community_events"

    def _get_events(self) -> List['CommunityEvent']:
        if self.events is None or self._are_events_expired():
            from demo.community_events import get_community_events
            logger.debug("Getting events from website.")
            self.last_event_update = datetime.now()
            self.events = get_community_events()

        return self.events

    def _are_events_expired(self) -> bool:
        # events are expired after 1 hour
        return (
            self.last_event_update is None or
            (datetime.now() - self.last_event_update).total_seconds() > 3600)

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List['Event']:
        intent = tracker.latest_message['intent'].get('name')
        events = self._get_events()

        if not events:
            dispatcher.utter_template("utter_no_community_event", tracker)
        elif intent == 'ask_which_events':
            self._utter_event_overview(dispatcher)
        elif intent == 'ask_when_next_event':
            self._utter_next_event(tracker, dispatcher)

        return []

    def _utter_event_overview(self,
                              dispatcher: CollectingDispatcher) -> None:
        events = self._get_events()
        event_items = ["- {} in {}".format(e.name_as_link(), e.city)
                       for e in events]
        locations = "\n".join(event_items)
        dispatcher.utter_message("Here are the next Rasa events:\n"
                                 "" + locations +
                                 "\nWe hope to see you at them!")

    def _utter_next_event(self,
                          tracker: Tracker,
                          dispatcher: CollectingDispatcher
                          ) -> None:
        location = next(tracker.get_latest_entity_values('location'), None)
        events = self._get_events()

        if location:
            events_for_location = [e for e in events
                                   if e.city == location or
                                   e.country == location]
            if not events_for_location and events:
                next_event = events[0]
                dispatcher.utter_template(
                    'utter_no_event_for_location_but_next',
                    tracker, **next_event.as_kwargs())
            elif events_for_location:
                next_event = events_for_location[0]
                dispatcher.utter_template('utter_next_event_for_location',
                                          tracker,
                                          **next_event.as_kwargs())
        elif events:
            next_event = events[0]
            dispatcher.utter_template('utter_next_event', tracker,
                                      **next_event.as_kwargs())


class ActionNextStep(Action):

    def name(self):
        return "action_next_step"

    def run(self, dispatcher, tracker, domain):
        step = int(tracker.get_slot('step'))+1

        if step in [2, 3, 4]:
            dispatcher.utter_template("utter_continue_step{}".format(step),
                                      tracker)
        else:
            dispatcher.utter_template("utter_no_more_steps", tracker)

        return []
