import pytest
import requests
import datetime
import uuid

from rasa_sdk.events import SlotSet

from actions import actions


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


def test_action_submit_sales_form(tracker, dispatcher, domain, gdrive):
    collected_info = {
        "company": "Sara CI",
        "use_case": "Unit Tests",
        "budget": "1000",
        "date": datetime.datetime.now().strftime("%d/%m/%Y"),
        # by using a random name we can verify that the line written to the spreadsheet is the one the test wrote
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
    tracker, dispatcher, domain, mailchimp_unsubscribed_email
):
    tracker.slots["email"] = mailchimp_unsubscribed_email
    action = actions.ActionSubmitSubscribeNewsletterForm()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1
    assert dispatcher.messages[0]["template"] == "utter_confirmationemail"


def test_action_submit_subscribe_newsletter_form_new(
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


def test_action_community_events(tracker, dispatcher, domain):
    action = actions.ActionCommunityEvent()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == []
    assert len(dispatcher.messages) == 1
