import requests
import re

from actions.api.discourse import DiscourseAPI


def test_get_discourse_links():
    """Test that the link returned is correctly formatted and goes to a valid webpage"""
    discourse = DiscourseAPI("https://forum.rasa.com/search")
    disc_res = discourse.query("rasa")
    disc_res = disc_res.json()
    link_string = discourse.get_discourse_links(disc_res.get("topics"), 0)
    markdown_link_pattern = r"- \[[^\]]+\]\([^\)]+\)$"
    assert re.match(markdown_link_pattern, link_string)

    link = link_string.split("](")[1][:-1]
    link_result = requests.get(link)
    assert link_result.status_code == 200
