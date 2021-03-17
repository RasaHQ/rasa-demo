import json
import pytest
import requests
import datetime
import pickle
import logging
import uuid

from rasa_sdk.executor import CollectingDispatcher, Tracker
from rasa_sdk.events import SlotSet, ActionExecuted, SessionStarted

from actions import actions, config
from actions.api.algolia import AlgoliaAPI
from actions.api.discourse import DiscourseAPI
from actions.api import community_events
from actions.api.gdrive_service import GDriveService


@pytest.mark.parametrize(
    "feedback_value, expected_tags",
    [
        ("positive", [{"value": "postive feedback"}]),
        ("negative", [{"value": "negative feedback"}]),
        ("other", []),
    ],
)
def test_action_tag_feedback(
    tracker,
    dispatcher,
    domain,
    feedback_value,
    expected_tags,
    rasa_x_convo,
    rasa_x_auth_header,
    rasa_x_conversation_endpoint,
):
    tracker.slots["feedback_value"] = feedback_value
    action = actions.ActionTagFeedback()
    actual_events = action.run(dispatcher, tracker, domain)
    expected_events = []
    assert actual_events == expected_events

    tag_response = requests.get(
        f"{rasa_x_conversation_endpoint}/{tracker.sender_id}/tags",
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
    tracker,
    dispatcher,
    domain,
    intent,
    expected_tags,
    rasa_x_convo,
    rasa_x_auth_header,
    rasa_x_conversation_endpoint,
):
    tracker.latest_message["intent"]["name"] = intent
    action = actions.ActionTagDocsSearch()
    actual_events = action.run(dispatcher, tracker, domain)
    expected_events = []
    assert actual_events == expected_events

    tag_response = requests.get(
        f"{rasa_x_conversation_endpoint}/{tracker.sender_id}/tags",
        headers=rasa_x_auth_header,
    )
    actual_tags = [{"value": tag.get("value")} for tag in tag_response.json()]
    assert actual_tags == expected_tags


def test_get_algolia_link():
    """Test that the link returned is correctly formatted and goes to a valid webpage"""
    # This could also stop at algolia.search and assert that the return matches the mocked API used for other tests
    algolia = AlgoliaAPI(
        config.algolia_app_id, config.algolia_search_key, config.algolia_docs_index
    )
    algolia_result = algolia.search("rasa")
    link_string = algolia.get_algolia_link(algolia_result.get("hits"), 0)
    link = link_string.split("](")[1][:-1]
    link_result = requests.get(link)
    assert link_result.status_code == 200


def test_get_discourse_links():
    """Test that the link returned is correctly formatted and goes to a valid webpage"""
    # This could also stop at discourse.query and assert that the return matches the mocked API used for other tests
    discourse = DiscourseAPI("https://forum.rasa.com/search")
    disc_res = discourse.query("rasa")
    disc_res = disc_res.json()
    link_string = discourse.get_discourse_links(disc_res.get("topics"), 0)
    link = link_string.split("](")[1][:-1]
    link_result = requests.get(link)
    assert link_result.status_code == 200


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
    tracker, dispatcher, domain, intent, entity, expected_events
):
    tracker.latest_message["intent"]["name"] = intent
    tracker.latest_message["entities"].append(entity)
    action = actions.ActionSetOnboarding()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == expected_events


def test_get_community_events(caplog):
    """
    Test that format of current events page is as expected and that parsing of a known events page finds the right events
    """
    with caplog.at_level(logging.WARNING):
        community_events.get_community_events()
    assert not caplog.text.startswith(
        "Error when trying to parse event details from html."
    )


def test_parse_community_events(mocker):
    mocker.patch.object(
        community_events,
        "get_community_page",
        return_value=pickle.load(open("tests/data/events_page.pkl", "rb")),
    )
    actual_events = [
        event.as_kwargs() for event in community_events.get_community_events()
    ]

    expected_events = [
        community_events.CommunityEvent(
            "WeAreDevelopers",
            "Berlin",
            "Germany",
            "28 – June 29, 2021",
            datetime.date.max,
            "https://www.wearedevelopers.com/events/world-congress/",
        ).as_kwargs()
    ]

    assert actual_events == expected_events


def test_action_submit_subscribe_newsletter_form_notsubscribed(
    tracker, dispatcher, domain, mailchimp_new_email
):

    tracker.slots["email"] = mailchimp_new_email
    action = actions.ActionSubmitSubscribeNewsletterForm()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_confirmationemail"


def test_action_submit_subscribe_newsletter_form_subscribed(
    tracker, dispatcher, domain, mailchimp_subscribed_email
):
    tracker.slots["email"] = mailchimp_subscribed_email
    action = actions.ActionSubmitSubscribeNewsletterForm()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_already_subscribed"


def test_action_submit_sales_form(tracker, dispatcher, domain, mocker, gdrive_sheet):
    company = "Sara CI"
    use_case = "Unit Tests"
    budget = "1000"
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    # by using a random name we can verify that the line written to the spreadsheet is the one the test wrote
    name = uuid.uuid1().hex
    job_function = "Test Actions"
    email = "example@rasa.com"

    tracker.slots["budget"] = budget
    tracker.slots["company"] = company
    tracker.slots["business_email"] = email
    tracker.slots["job_function"] = job_function
    tracker.slots["person_name"] = name
    tracker.slots["use_case"] = use_case

    sheet_name = gdrive_sheet[0]
    worksheet = gdrive_sheet[1]
    row_values = [company, use_case, budget, date, name, job_function, email]

    mocker.patch.object(GDriveService, "SHEET_NAME", sheet_name)
    action = actions.ActionSubmitSalesForm()
    actual_events = action.run(dispatcher, tracker, domain)

    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_confirm_salesrequest"
    assert worksheet.row_values(2) == row_values
