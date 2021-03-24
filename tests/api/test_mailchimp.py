import pytest

from actions import config
from actions.api.mailchimp import MailChimpAPI


@pytest.mark.parametrize(
    "email, validity", [("valid.email@rasa.com", True), ("notanemail", False)],
)
def test_is_valid_email(email, validity):
    actual_validity = MailChimpAPI.is_valid_email(email)
    assert actual_validity == validity


@pytest.mark.parametrize(
    "email, hash", [("valid.email@rasa.com", "c60f89d8592b8eebb2a463d78d37c0ee")],
)
def test_hash_email(email, hash):
    actual_hash = MailChimpAPI.hash_email(email)
    assert actual_hash == hash


def test_subscribe_user_new(mailchimp_new_email):
    client = MailChimpAPI(config.mailchimp_api_key)
    actual_subscribed = client.subscribe_user(
        config.mailchimp_list, mailchimp_new_email
    )
    assert actual_subscribed is True


def test_subscribe_user_subscribed(mailchimp_subscribed_email):
    client = MailChimpAPI(config.mailchimp_api_key)
    actual_subscribed = client.subscribe_user(
        config.mailchimp_list, mailchimp_subscribed_email
    )
    assert actual_subscribed is False


def test_subscribe_user_unsubscribed(mailchimp_unsubscribed_email):
    client = MailChimpAPI(config.mailchimp_api_key)
    actual_subscribed = client.subscribe_user(
        config.mailchimp_list, mailchimp_unsubscribed_email
    )
    assert actual_subscribed is True
