import json
import pytest
import requests
import datetime
import pickle

from rasa_sdk.executor import CollectingDispatcher, Tracker
from rasa_sdk.events import SlotSet, ActionExecuted, SessionStarted

from actions import actions, config
from actions.api.algolia import AlgoliaAPI
from actions.api.discourse import DiscourseAPI
from actions.api import community_events



@pytest.mark.parametrize(
    "feedback_value, expected_tags", [
        ("positive",[{"value":"postive feedback"}]),
        ("negative", [{"value":"negative feedback"}]),
        ("other",[])
    ]
)
def test_run_action_tag_feedback(tracker, dispatcher, domain, feedback_value, expected_tags, rasa_x_convo):
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


@pytest.mark.parametrize(
    "intent, expected_tags", [
        ("affirm",[{"value":"docs search helpful"}]),
        ("deny", [{"value":"docs search unhelpful"}]),
        ("other",[])
    ]
)
def test_run_action_tag_docs_search(tracker, dispatcher, domain, intent, expected_tags, rasa_x_convo):
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

def test_get_algolia_link():
    """Test that the link returned is correctly formatted and goes to a valid webpage
    """
    # This could also stop at algolia.search and assert that the return matches the mocked API used for other tests
    algolia = AlgoliaAPI(
            config.algolia_app_id, config.algolia_search_key, config.algolia_docs_index
        )
    algolia_result = algolia.search("rasa")
    link_string = algolia.get_algolia_link(algolia_result.get("hits"),0)
    link = link_string.split("](")[1][:-1]
    link_result = requests.get(link)
    assert link_result.status_code == 200

def test_get_discourse_links():
    """Test that the link returned is correctly formatted and goes to a valid webpage
    """
    # This could also stop at discourse.query and assert that the return matches the mocked API used for other tests
    discourse = DiscourseAPI("https://forum.rasa.com/search")
    disc_res = discourse.query("rasa")
    disc_res = disc_res.json()
    link_string = discourse.get_discourse_links(disc_res.get("topics"), 0)
    link = link_string.split("](")[1][:-1]
    link_result = requests.get(link)
    assert link_result.status_code == 200

def test_get_community_events(monkeypatch):
    """
    Test that format of current events page is as expected and that parsing of a known events page finds the right events
    """
    with pytest.warns(None) as record:
        community_events.get_community_events()
    assert len(record) == 0

    monkeypatch.setattr(requests, "get", pickle.load(open("tests/data/events_page.pkl","rb")))
    with pytest.warns(None) as record:
        actual_events = [event.as_kwargs() for event in community_events.get_community_events()]

    expected_events = [community_events.CommunityEvent(
        "WeAreDevelopers",
        "Berlin",
        "Germany",
        "28 – June 29, 2021",
        datetime.date.max,
        "https://www.wearedevelopers.com/events/world-congress/"
        ).as_kwargs()
    ]

    assert len(record) == 0
    assert actual_events == expected_events



@pytest.mark.parametrize(
    "intent, entity, expected_events", [
        ("how_to_get_started", {"entity": "user_type", "value": "new"}, [SlotSet("onboarding", True)]),
        ("affirm",{},[SlotSet("onboarding",True)]),
        ("deny",{},[SlotSet("onboarding",False)]),
        ("other",{"entity":"user_type","value":"new"},[])
    ]
)
def test_action_set_onboarding(tracker, dispatcher, domain, intent, entity, expected_events):
    tracker.latest_message["intent"]["name"] = intent
    tracker.latest_message["entities"].append(entity)
    action = actions.ActionSetOnboarding()
    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events == expected_events

