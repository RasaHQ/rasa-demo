# -*- coding: utf-8 -*-
from typing import Text
import requests
import logging

from rasa_sdk import Tracker

from actions import config

logger = logging.getLogger(__name__)


class RasaXAPI:
    """Class to connect to the Rasa X API"""
    schema = config.rasa_x_host_schema
    host = config.rasa_x_host
    username = config.rasa_x_username
    password = config.rasa_x_password

    @classmethod
    def get_auth_header(cls):
        """
        get authorization header with bearer token if authentication succeeds
        """
        url = f"{cls.schema}://{cls.host}/api/auth"
        payload = {"username": cls.username, "password": cls.password}
        response = requests.post(url, json=payload)
        try:
            authtoken = response.json()["access_token"]
            header = {"Authorization": f"Bearer {authtoken}"}
            return header
        except:
            return {}

    @classmethod
    def tag_convo(cls, tracker: Tracker, label: Text) -> None:
        """Tag a conversation in Rasa X with a given label"""
        auth_header = cls.get_auth_header()
        endpoint = f"{cls.schema}://{cls.host}/api/conversations/{tracker.sender_id}/tags"
        response = requests.post(url=endpoint, data = label, headers=auth_header)
        return response
