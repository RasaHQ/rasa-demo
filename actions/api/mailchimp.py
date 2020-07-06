# -*- coding: utf-8 -*-

from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from mailchimp3.helpers import check_email
from typing import Text
import logging

logger = logging.getLogger(__name__)


class MailChimpAPI:
    """Class to connect to the MailChimp API"""

    def __init__(self, api_key: Text) -> None:

        self.client = MailChimp(mc_api=api_key)

    @staticmethod
    def is_valid_email(email: Text) -> bool:
        """Use mailchimp3 helper function to validate that it will accept it as a valid
        email"""
        try:
            email = str(email)
            check_email(email)
            return True
        except ValueError:  # purposely raised in case of invalid email
            return False
        except Exception as e:
            logger.warning(
                f"Error: exception in check_email.\n"
                f"{type(e)} - {e}\n"
                f"email = {email}\n"
                f"type(email) = {type(email)}"
            )
            return False

    def subscribe_user(self, list_id: Text, email: Text) -> bool:
        # subscribe the user to the newsletter if they're not already
        # subscribed, with the status pending
        try:
            self.client.lists.members.create(
                list_id, data={"email_address": email, "status": "pending"}
            )
            return True

        # if the user is already subscribed, return False
        except MailChimpError:
            return False
