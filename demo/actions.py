# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from demo.api import MailChimpAPI
from demo import config

logger = logging.getLogger(__name__)


class ActionSubscribeNewsletter(Action):

    def name(self):
        return "action_subscribe_newsletter"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email')
        if email:
            client = MailChimpAPI(config.mailchimp_api_key)
            subscribed = client.subscribe_user(config.mailchimp_list, email)

            return [SlotSet('subscribed', subscribed)]
