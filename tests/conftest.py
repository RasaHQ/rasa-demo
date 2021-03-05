import os
from pathlib import Path
import pytest
import json
import requests

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from actions import config

here = Path(__file__).parent.resolve()

@pytest.fixture
def tracker():
    return Tracker.from_dict(json.load(open(here / "./data/initial_tracker.json")))


@pytest.fixture
def dispatcher():
    return CollectingDispatcher()


@pytest.fixture
def domain():
    return dict()


@pytest.fixture
def rasa_x_convo(tracker):
    auth_endpoint = f"http://{config.rasa_x_host}/api/auth"
    auth_data = {
        "username": config.rasa_x_username,
        "password": config.rasa_x_password
    }
    auth_response = requests.post(url=auth_endpoint, json=auth_data)

    endpoint = f"http://{config.rasa_x_host}/api/conversations"
    data = {
        "sender_id": tracker.sender_id
    }
    headers = {"Authorization": f"Bearer {auth_response.json()['access_token']}"}
    response = requests.post(endpoint, json=data, headers=headers)
    
    yield (endpoint, headers)
    
    del_endpoint = f"http://{config.rasa_x_host}/api/conversations/{tracker.sender_id}"
    del_response = requests.delete(del_endpoint, headers=headers)
