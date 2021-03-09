# -*- coding: utf-8 -*-

from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from mailchimp3.helpers import check_email
import hashlib
from typing import Text
import logging

logger = logging.getLogger(__name__)


class MailChimpAPI:
    """Class to connect to the MailChimp API"""

    def __init__(self, api_key: Text) -> None:

        self.client = MailChimp(mc_api=api_key)

    @staticmethod
    def hash_email(email: Text) -> Text:
        """Create an md5 hash of an email address"""
        encoded_email = email.lower().encode(encoding='utf-8')
        hash = hashlib.md5(encoded_email).hexdigest()
        return hash
 

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

        
        except MailChimpError:
            try:
                hash = self.hash_email(email)
                status = self.client.lists.members.get(list_id, hash).get("status")
                if status != "subscribed" and status != "pending":
                    # if user is in database, but is unsubscribed or archived, attempt to resubscribe
                    self.client.lists.members.update(
                        list_id, hash, data={"email_address": email, "status": "pending"}
                    )
                    return True
                return False
            except MailChimpError:
                return False


    def unsubscribe_user(self, list_id: Text, email: Text):
        hash = self.hash_email(email)
        self.client.lists.members.update(list_id, hash, {"status": "unsubscribed"})


