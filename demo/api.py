# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from hashlib import md5


class MailChimpAPI(object):

    def __init__(self, api_key):

        self.client = MailChimp(mc_api=api_key)

    def get_all_members(self):
        list = self.client.lists.members.all('297618692e', get_all=True)

    def check_subscribed(self, list_id, email):
        hashed_email = md5(email.lower()).hexdigest()
        user = self.client.lists.members.get(list_id=list_id,
                                             subscriber_hash=hashed_email).json()

        return user

    def subscribe_user(self, list_id, email):
        try:
            self.client.lists.members.create(list_id, data={
                                'email_address': email,
                                'status': 'pending'})
            return True

        except MailChimpError:
            return False
