import requests

from actions.api.rasaxapi import RasaXAPI


def test_get_auth():
    rasax = RasaXAPI()
    actual_auth_headers = rasax.get_auth_header()
    assert set(actual_auth_headers.keys()) == {"Authorization"}
    assert actual_auth_headers["Authorization"].startswith("Bearer ")


def test_tag_convo(
    tracker, rasa_x_convo, rasa_x_auth_header, rasa_x_conversation_endpoint,
):
    tag = {"value": "test"}
    labeldata = '[{"value":"test","color":"76af3c"}]'
    rasax = RasaXAPI()
    rasax.tag_convo(tracker, labeldata)
    tag_response = requests.get(
        f"{rasa_x_conversation_endpoint}/{tracker.sender_id}/tags",
        headers=rasa_x_auth_header,
    )
    actual_tags = [{"value": tag.get("value")} for tag in tag_response.json()]
    assert actual_tags == [tag]
