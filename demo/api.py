# -*- coding: utf-8 -*-

from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from typing import Text


class MailChimpAPI:
    """Class to connect to the MailChimp API"""

    def __init__(self, api_key: Text) -> None:

        self.client = MailChimp(mc_api=api_key)

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
