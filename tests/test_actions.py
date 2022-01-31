"""Unit tests for the custom actions"""
import pytest
import requests
import datetime
import uuid
from typing import Text, Dict, Tuple, List
from gspread.models import Worksheet

from rasa_sdk.events import (
    EventType,
    SlotSet,
    UserUtteranceReverted,
)
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from rasa_sdk.types import DomainDict

from actions import actions
from actions.api.gdrive_service import GDriveService
from actions.actions import USER_INTENT_OUT_OF_SCOPE


@pytest.mark.parametrize(
    "feedback_value, expected_tags",
    [
        ("positive", [{"value": "postive feedback"}]),
        ("negative", [{"value": "negative feedback"}]),
        ("other", []),
    ],
)
def test_action_tag_feedback(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    feedback_value: Text,
    expected_tags: List[Dict],
    rasa_x_convo: None,
    rasa_x_auth_header: Dict[Text, Text],
    rasa_x_conversation_endpoint: Text,
):
    tracker.slots["feedback_value"] = feedback_value
    action = actions.ActionTagFeedback()
    actual_events = action.run(dispatcher, tracker, domain)
    expected_events = []
    assert actual_events == expected_events

    tag_response = requests.get(
        f"{rasa_x_conversation_endpoint}/{tracker.sender_id}/data-tags",
        headers=rasa_x_auth_header,
    )
    actual_tags = [{"value": tag.get("value")} for tag in tag_response.json()]
    assert actual_tags == expected_tags


@pytest.mark.parametrize(
    "intent, expected_tags",
    [
        ("affirm", [{"value": "docs search helpful"}]),
        ("deny", [{"value": "docs search unhelpful"}]),
        ("other", []),
    ],
)
def test_action_tag_docs_search(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    intent: Text,
    expected_tags: List[Dict],
    rasa_x_convo: None,
    rasa_x_auth_header: Dict[Text, Text],
    rasa_x_conversation_endpoint: Text,
):
    tracker.latest_message["intent"]["name"] = intent
    action = actions.ActionTagDocsSearch()
    actual_events = action.run(dispatcher, tracker, domain)
    expected_events = []
    assert actual_events == expected_events

    tag_response = requests.get(
        f"{rasa_x_conversation_endpoint}/{tracker.sender_id}/data-tags",
        headers=rasa_x_auth_header,
    )
    actual_tags = [{"value": tag.get("value")} for tag in tag_response.json()]
    assert actual_tags == expected_tags


@pytest.mark.parametrize(
    "intent, entity, expected_events",
    [
        (
            "how_to_get_started",
            {"entity": "user_type", "value": "new"},
            [SlotSet("onboarding", True)],
        ),
        ("affirm", {}, [SlotSet("onboarding", True)]),
        ("deny", {}, [SlotSet("onboarding", False)]),
        ("other", {"entity": "user_type", "value": "new"}, []),
    ],
)
def test_action_set_onboarding(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    intent: Text,
    entity: Dict[Text, Text],
    expected_events: List[EventType],
):
    tracker.latest_message["intent"]["name"] = intent
    tracker.latest_message["entities"].append(entity)
    action = actions.ActionSetOnboarding()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == expected_events


def test_action_submit_sales_form(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    gdrive: Tuple[GDriveService, Worksheet],
):
    collected_info = {
        "company": "Sara CI",
        "use_case": "Unit Tests",
        "budget": "1000",
        "date": datetime.datetime.now().strftime("%d/%m/%Y"),
        # by using a random name we can verify that the line written to the spreadsheet
        # is the one the test wrote
        "person_name": uuid.uuid1().hex,
        "job_function": "Test Actions",
        "business_email": "example@rasa.com",
    }
    tracker.slots.update(collected_info)

    worksheet = gdrive[1]
    row_values = [
        collected_info["company"],
        collected_info["use_case"],
        collected_info["budget"],
        collected_info["date"],
        collected_info["person_name"],
        collected_info["job_function"],
        collected_info["business_email"],
    ]

    action = actions.ActionSubmitSalesForm()
    actual_events = action.run(dispatcher, tracker, domain)

    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_confirm_salesrequest"
    assert worksheet.row_values(2) == row_values


def test_action_submit_subscribe_newsletter_form_unsubscribed(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    mailchimp_unsubscribed_email: Text,
):
    tracker.slots["email"] = mailchimp_unsubscribed_email
    action = actions.ActionSubmitSubscribeNewsletterForm()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_confirmationemail"


def test_action_submit_subscribe_newsletter_form_new(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    mailchimp_email: Text,
):
    tracker.slots["email"] = mailchimp_email
    action = actions.ActionSubmitSubscribeNewsletterForm()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_confirmationemail"


def test_action_submit_subscribe_newsletter_form_subscribed(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    mailchimp_subscribed_email: Text,
):
    tracker.slots["email"] = mailchimp_subscribed_email
    action = actions.ActionSubmitSubscribeNewsletterForm()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_already_subscribed"


def test_action_community_events(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
):
    action = actions.ActionCommunityEvent()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1


@pytest.mark.parametrize(
    "last_intent, expected_events",
    [
        (USER_INTENT_OUT_OF_SCOPE, [SlotSet("feedback_value", "negative")]),
        ("bye", [UserUtteranceReverted()]),
    ],
)
def test_action_default_fallback(
    tracker: Tracker,
    dispatcher: CollectingDispatcher,
    domain: DomainDict,
    last_intent,
    expected_events,
):

    tracker.latest_message["intent"]["name"] = last_intent

    action = actions.ActionDefaultFallback()
    actual_events = action.run(dispatcher, tracker, domain)

    assert actual_events == expected_events
