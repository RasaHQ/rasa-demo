# -*- coding: utf-8 -*-

import logging

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
                                 ConversationPaused

from demo.api import MailChimpAPI
from demo import config
from demo.gdrive_service import GDriveService

logger = logging.getLogger(__name__)


class ActionSubscribeNewsletter(Action):
    """ This action calls our newsletter API and subscribes the user with
    their email address"""

    def name(self):
        return "action_subscribe_newsletter"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email')
        if email:
            client = MailChimpAPI(config.mailchimp_api_key)
            # if the email is already subscribed, this returns False
            subscribed = client.subscribe_user(config.mailchimp_list, email)

            return [SlotSet('subscribed', subscribed)]
        return []


class ActionStoreSalesInfo(Action):
    """Saves the information collected in the sales flow into a spreadsheet"""

    def name(self):
        return "action_store_sales_info"

    def run(self, dispatcher, tracker, domain):
        import datetime
        budget = tracker.get_slot('budget')
        company = tracker.get_slot('company_name')
        email = tracker.get_slot('email')
        jobfunction = tracker.get_slot('job_function')
        name = tracker.get_slot('person_name')
        use_case = tracker.get_slot('use_case')
        date = datetime.datetime.now().strftime("%d/%m/%Y")

        sales_info = [company, use_case, budget, date, name, jobfunction,
                      email]

        gdrive = GDriveService()
        try:
            gdrive.store_data(sales_info)
            return [SlotSet('data_stored', True)]
        except Exception as e:
            logger.error("Failed to write data to gdocs. Error: {}"
                         "".format(e.message), exc_info=True)
            return [SlotSet('data_stored', False)]


class ActionStoreBudget(Action):
    """Stores the budget in a slot"""

    def name(self):
        return "action_store_budget"

    def run(self, dispatcher, tracker, domain):

        # the entity can be one of two entities from duckling,
        # number or amount-of-money
        budget = next(tracker.get_latest_entity_values('number'), None)
        if not budget:
            budget = next(tracker.get_latest_entity_values('amount-of-money'),
                          None)

        # as a fallback, if no entity is recognised (e.g. in a sentence
        # like "I have no money") we store the whole user utterance in the slot
        # In future this should be stored in a `budget_unconfirmed` slot where
        # the user will then be asked to confirm this is there budget
        if not budget:
            budget = tracker.latest_message.get('text')

        return [SlotSet('budget', budget)]


class ActionStoreUsecase(Action):
    """Stores the bot use case in a slot"""

    def name(self):
        return "action_store_usecase"

    def run(self, dispatcher, tracker, domain):

        # we grab the whole user utterance here as there are no real entities
        # in the use case
        use_case = tracker.latest_message.get('text')

        return [SlotSet('use_case', use_case)]


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):

        intent = tracker.latest_message.intent.get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_builder', 'ask_howdoing', 'ask_weather',
                      'ask_whatspossible', 'ask_whoisit', 'ask_whatisrasa',
                      'ask_isbot']:
            dispatcher.utter_template('utter_' + intent, tracker)
        return []


class ActionStoreName(Action):
    """Stores the users name in a slot"""

    def name(self):
        return "action_store_name"

    def run(self, dispatcher, tracker, domain):

        person_name = next(tracker.get_latest_entity_values('name'), None)

        # if no name was extracted, use the whole user utterance
        # in future this will be stored in a `name_unconfirmed` slot and the
        # user will be asked to confirm their name
        if not person_name:
            person_name = tracker.latest_message.get('text')

        return [SlotSet('person_name', person_name)]


class ActionStoreCompany(Action):
    """Stores the company name in a slot"""

    def name(self):
        return "action_store_company"

    def run(self, dispatcher, tracker, domain):
        company = next(tracker.get_latest_entity_values('company'), None)

        # if no company entity was extracted, use the whole user utterance
        # in future this will be stored in a `company_unconfirmed` slot and
        # the user will be asked to confirm their company name
        if not company:
            company = tracker.latest_message.get('text')

        return [SlotSet('company_name', company)]


class ActionStoreJob(Action):
    """Stores the job in a slot"""

    def name(self):
        return "action_store_job"

    def run(self, dispatcher, tracker, domain):
        jobfunction = next(tracker.get_latest_entity_values('jobfunction'),
                           None)

        # if no jobfunction entity was extracted, use the whole user utterance
        # in future this will be stored in a `job_unconfirmed` slot and
        # the user will be asked to confirm their job title
        if not jobfunction:
            jobfunction = tracker.latest_message.get('text')

        return [SlotSet('job_function', jobfunction)]


class ActionStoreEmail(Action):
    """Stores the email in a slot"""

    def name(self):
        return "action_store_email"

    def run(self, dispatcher, tracker, domain):
        email = next(tracker.get_latest_entity_values('email'), None)

        # if no email entity was recognised, prompt the user to enter a valid
        # email and go back a turn in the conversation to ensure future
        # predictions aren't affected
        if not email:
            dispatcher.utter_message("We need your email, please enter a valid one.")
            return [UserUtteranceReverted()]

        return [SlotSet('email', email)]


class ActionPause(Action):
    """Pause the conversation"""

    def name(self):
        return "action_pause"

    def run(self, dispatcher, tracker, domain):

        return [ConversationPaused()]
