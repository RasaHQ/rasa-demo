import requests
import re

from actions import config
from actions.api.algolia import AlgoliaAPI


def test_get_algolia_link():
    """Test that the link returned is correctly formatted and goes to a valid webpage"""
    algolia = AlgoliaAPI(
        config.algolia_app_id, config.algolia_search_key, config.algolia_docs_index
    )
    algolia_result = algolia.search("rasa")
    link_string = algolia.get_algolia_link(algolia_result.get("hits"), 0)
    markdown_link_pattern = r"- \[[^\]]+\]\([^\)]+\)$"
    assert re.match(markdown_link_pattern, link_string)

    link = link_string.split("](")[1][:-1]
    link_result = requests.get(link)
    assert link_result.status_code == 200
