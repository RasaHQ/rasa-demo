import os
import pytest
import json
import requests

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from rasa.shared.core.domain import Domain
from mailchimp3.mailchimpclient import MailChimpError

from actions import config
from actions.api.rasaxapi import RasaXAPI
from actions.api.mailchimp import MailChimpAPI
from actions.api.gdrive_service import GDriveService


@pytest.fixture
def tracker():
    """Load a tracker object"""
    with open("tests/data/initial_tracker.json") as json_file:
        tracker = Tracker.from_dict(json.load(json_file))
    return tracker


@pytest.fixture
def dispatcher():
    """Create a clean dispatcher"""
    return CollectingDispatcher()


@pytest.fixture
def domain():
    """Load the domain, return as a dictionary"""
    domain = Domain.load("domain.yml")
    return domain.as_dict()


@pytest.fixture
def rasa_x_conversation_endpoint():
    """Return Rasa X conversations endpoint"""
    return f"{RasaXAPI.schema}://{RasaXAPI.host}/api/conversations"


@pytest.fixture
def rasa_x_auth_header():
    """Get authentication header for Rasa X"""
    return RasaXAPI.get_auth_header()


@pytest.fixture
def rasa_x_convo(rasa_x_conversation_endpoint, rasa_x_auth_header, tracker):
    """Create an empty conversation in Rasa X"""
    del_endpoint = f"{rasa_x_conversation_endpoint}/{tracker.sender_id}"
    # delete the conversation in case it already exists due to an improperly exited test
    requests.delete(del_endpoint, headers=rasa_x_auth_header)

    data = {"sender_id": tracker.sender_id}
    requests.post(rasa_x_conversation_endpoint, json=data, headers=rasa_x_auth_header)

    yield

    requests.delete(del_endpoint, headers=rasa_x_auth_header)


@pytest.fixture
def mailchimp_new_email():
    """Create a user who is not already subscribed to the newsletter"""
    email = "example@rasa.com"
    client = MailChimpAPI(config.mailchimp_api_key)
    client.unsubscribe_user(config.mailchimp_list, email)
    yield email
    client.unsubscribe_user(config.mailchimp_list, email)


@pytest.fixture
def mailchimp_subscribed_email():
    """Create a user who is already subscribed to the newsletter"""
    email = "example_subscribed@rasa.com"
    client = MailChimpAPI(config.mailchimp_api_key)
    client.subscribe_user(config.mailchimp_list, email)
    yield email
    client.unsubscribe_user(config.mailchimp_list, email)


@pytest.fixture
def gdrive_sheet():
    """Clear test sheet to allow asserting contents of rows"""
    test_sheet = "demobot_testing"
    gdrive = GDriveService()
    gdrive.SHEET_NAME = test_sheet
    spreadsheet_name = gdrive.SPREADSHEET_NAME
    spreadsheet = gdrive.request_sheet(spreadsheet_name)
    worksheet = spreadsheet.worksheet(test_sheet)
    worksheet.resize(rows=1)

    yield test_sheet, worksheet

    worksheet.resize(rows=1)
