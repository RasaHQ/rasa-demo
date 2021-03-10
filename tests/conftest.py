import os
from pathlib import Path
import pytest
import json
import requests

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from mailchimp3.mailchimpclient import MailChimpError

from actions import config
from actions.api.rasaxapi import RasaXAPI
from actions.api.mailchimp import MailChimpAPI
from actions.api.gdrive_service import GDriveService

here = Path(__file__).parent.resolve()

@pytest.fixture
def tracker():
    tracker = Tracker.from_dict(json.load(open(here / "./data/initial_tracker.json")))
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
    del_endpoint = f"{rasa_x_conversation_endpoint}/{tracker.sender_id}"
    # delete the conversation in case it already exists due to an improperly exited test
    requests.delete(del_endpoint, headers=rasa_x_auth_header)

    data = {"sender_id": tracker.sender_id}
    requests.post(rasa_x_conversation_endpoint, json=data, headers=rasa_x_auth_header)

    yield
    
    requests.delete(del_endpoint, headers=rasa_x_auth_header)

@pytest.fixture
def mailchimp_new_email():
    """make sure the fake email is not already subscribed, and delete it again once test completes"""
    email = "example@rasa.com"
    client = MailChimpAPI(config.mailchimp_api_key)
    client.unsubscribe_user(config.mailchimp_list, email)
    yield email
    client.unsubscribe_user(config.mailchimp_list, email)

@pytest.fixture
def mailchimp_subscribed_email():
    """make sure the fake email is subscribed"""
    email = "example_subscribed@rasa.com"
    client = MailChimpAPI(config.mailchimp_api_key)
    client.subscribe_user(config.mailchimp_list, email)
    yield email

@pytest.fixture
def gdrive_sheet():
    """make sure test sheet has only one row before test starts and delete any created rows once the test finishes"""
    test_sheet = "demobot_testing"
    gdrive = GDriveService()
    gdrive.SHEET_NAME = test_sheet
    spreadsheet_name = gdrive.SPREADSHEET_NAME
    spreadsheet = gdrive.request_sheet(spreadsheet_name)
    worksheet = spreadsheet.worksheet(test_sheet)
    worksheet.resize(rows=1)

    yield test_sheet, worksheet

    worksheet.resize(rows=1)

    
