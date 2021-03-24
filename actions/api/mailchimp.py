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
        encoded_email = email.lower().encode(encoding="utf-8")
        hash = hashlib.md5(encoded_email).hexdigest()
        return hash

    @staticmethod
    def is_valid_email(email: Text) -> bool:
        """Validate that mailchimp will accept email as valid"""
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

    def subscribe_user(self, list_id: Text, email: Text) -> Text:
        """Subscribe the user to the newsletter if they're not already"""
        try:
            # subscribe a user who is not in the database at all to the newsletter.
            # Will fail if they are already in database
            self.client.lists.members.create(
                list_id, data={"email_address": email, "status": "pending"}
            )
            return "newly_subscribed"

        except MailChimpError:
            # user is already in the database, or new user creation failed for another reason, try to update the user
            try:
                hash = self.hash_email(email)
                # check status of user already in database. Will throw exception if they are not in database.
                status = self.client.lists.members.get(list_id, hash).get("status")
                if status in ["subscribed", "pending"]:
                    # if user is already subscribed, can't subscribe again
                    return "already_subscribed"
                else:
                    # if user is in database, but is unsubscribed or archived, attempt to resubscribe
                    self.client.lists.members.update(
                        list_id,
                        hash,
                        data={"email_address": email, "status": "pending"},
                    )
                    return "newly_subscribed"

            except MailChimpError:
                # if the subscription of an unsubscribed user fails, some other error occurred
                # like e.g. a permanently deleted user attempting to resubscribe
                return "error"

    def unsubscribe_user(self, list_id: Text, email: Text):
        hash = self.hash_email(email)
        self.client.lists.members.update(list_id, hash, {"status": "unsubscribed"})

    def delete_user(self, list_id: Text, email: Text):
        """
        Unsubscribes and then permanently deletes a member from the mailing list.
        Note that after permanent deletion, MailChimp does not allow resubscription of the deleted address
        via the API.
        """
        self.unsubscribe_user(list_id, email)
        hash = self.hash_email(email)
        self.client.lists.members.delete_permanent(list_id, hash)
