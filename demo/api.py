# -*- coding: utf-8 -*-

from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from mailchimp3.helpers import check_email
from typing import Text


class MailChimpAPI:
    """Class to connect to the MailChimp API"""

    def __init__(self, api_key: Text) -> None:

        self.client = MailChimp(mc_api=api_key)

    @staticmethod
    def is_valid_email(email: Text) -> bool:
        """Use mailchimp3 helper function to validate that it will accept it as a valid
        email"""
        try:
            check_email(email)
            return True
        except (TypeError, ValueError):
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
