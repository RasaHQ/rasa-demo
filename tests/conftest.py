import os
from pathlib import Path
import pytest
import json
import requests
import uuid

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from actions import config
from actions.api.rasaxapi import RasaXAPI

here = Path(__file__).parent.resolve()

@pytest.fixture
def tracker():
    tracker = Tracker.from_dict(json.load(open(here / "./data/initial_tracker.json")))
    # pytest appears not to wait long enough for convo to be deleted. 
    # using random uuid prevents errors due to previous tests' actions on test conversation
    tracker.sender_id = uuid.uuid4().hex 
    return tracker



@pytest.fixture
def dispatcher():
    return CollectingDispatcher()


@pytest.fixture
def domain():
    return dict()


@pytest.fixture
def rasa_x_conversation_endpoint():
    return f"{RasaXAPI.schema}://{RasaXAPI.host}/api/conversations"

@pytest.fixture
def rasa_x_auth_header():
    return RasaXAPI.get_auth_header()

@pytest.fixture
def rasa_x_convo(rasa_x_conversation_endpoint, rasa_x_auth_header, tracker):
    data = {"sender_id": tracker.sender_id}
    response = requests.post(rasa_x_conversation_endpoint, json=data, headers=rasa_x_auth_header)

    yield
    
    del_endpoint = f"{rasa_x_conversation_endpoint}/{tracker.sender_id}"
    del_response = requests.delete(del_endpoint, headers=rasa_x_auth_header)
