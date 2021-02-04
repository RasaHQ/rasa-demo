import json
import pytest
import requests

from rasa_sdk.executor import CollectingDispatcher, Tracker
from rasa_sdk.events import SlotSet, ActionExecuted, SessionStarted

from actions import actions

@pytest.mark.parametrize(
    "intent, expected_tags", [
        ("affirm",[{"value":"docs search helpful"}]),
        ("deny", [{"value":"docs search unhelpful"}]),
        ("other",[])
    ]
)
@pytest.mark.asyncio
async def test_run_action_tag_docs_search(tracker, dispatcher, domain, intent, expected_tags, rasa_x_convo):
    tracker.latest_message["intent"]["name"] = intent
    action = actions.ActionTagDocsSearch()
    actual_events = action.run(dispatcher, tracker, domain)
    expected_events = []
    assert actual_events == expected_events

    conversation_endpoint = rasa_x_convo[0]
    auth_headers = rasa_x_convo[1]
    tag_response = requests.get(f"{conversation_endpoint}/{tracker.sender_id}/tags", headers=auth_headers)
    actual_tags = [{"value":tag.get("value")} for tag in tag_response.json()]
    assert actual_tags == expected_tags

@pytest.mark.parametrize(
    "feedback_value, expected_tags", [
        ("positive",[{"value":"postive feedback"}]),
        ("negative", [{"value":"negative feedback"}]),
        ("other",[])
    ]
)
@pytest.mark.asyncio
async def test_run_action_tag_feedback(tracker, dispatcher, domain, feedback_value, expected_tags, rasa_x_convo):
    tracker.slots["feedback_value"] = feedback_value
    action = actions.ActionTagFeedback()
    actual_events = action.run(dispatcher, tracker, domain)
    expected_events = []
    assert actual_events == expected_events

    conversation_endpoint = rasa_x_convo[0]
    auth_headers = rasa_x_convo[1]
    tag_response = requests.get(f"{conversation_endpoint}/{tracker.sender_id}/tags", headers=auth_headers)
    actual_tags = [{"value":tag.get("value")} for tag in tag_response.json()]
    assert actual_tags == expected_tags
