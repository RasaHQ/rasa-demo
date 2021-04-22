import datetime
import pickle
import logging
from _pytest.logging import LogCaptureFixture
from pytest_mock import mocker

from actions.api import community_events


def test_get_community_events(caplog: LogCaptureFixture):
    """
    Test that format of current events page is as expected and that parsing of a known events page finds the right events
    """
    with caplog.at_level(logging.WARNING):
        community_events.get_community_events()
    assert "Error when trying to parse event details from html." not in caplog.text


def test_parse_community_events(mocker: mocker):
    with open("tests/data/events_page.pkl", "rb") as fh:
        mocker.patch.object(
            community_events,
            "get_community_page",
            return_value=pickle.load(fh),
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
