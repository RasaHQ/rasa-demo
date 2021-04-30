import pytest
from typing import Text
from mailchimp3 import MailChimp  # noqa: F401

from actions import config
from actions.api.mailchimp import MailChimpAPI


@pytest.mark.parametrize(
    "email, validity",
    [("valid.email@rasa.com", True), ("notanemail", False)],
)
def test_is_valid_email(email: Text, validity: bool):
    actual_validity = MailChimpAPI.is_valid_email(email)
    assert actual_validity == validity


@pytest.mark.parametrize(
    "email, hash",
    [("valid.email@rasa.com", "c60f89d8592b8eebb2a463d78d37c0ee")],
)
def test_hash_email(email: Text, hash: Text):
    actual_hash = MailChimpAPI.hash_email(email)
    assert actual_hash == hash


def test_subscribe_user_new(mailchimp_client: "MailChimp", mailchimp_email: Text):
    actual_subscription_status = mailchimp_client.subscribe_user(
        config.mailchimp_list, mailchimp_email
    )
    assert actual_subscription_status == "newly_subscribed"


def test_subscribe_user_subscribed(
    mailchimp_client: "MailChimp", mailchimp_subscribed_email: Text
):
    actual_subscription_status = mailchimp_client.subscribe_user(
        config.mailchimp_list, mailchimp_subscribed_email
    )
    assert actual_subscription_status == "already_subscribed"


def test_subscribe_user_unsubscribed(
    mailchimp_client: "MailChimp", mailchimp_unsubscribed_email: Text
):
    actual_subscription_status = mailchimp_client.subscribe_user(
        config.mailchimp_list, mailchimp_unsubscribed_email
    )
    assert actual_subscription_status == "newly_subscribed"
