# -*- coding: utf-8 -*-
from algoliasearch.search_client import SearchClient
from typing import Text, List


class AlgoliaAPI(object):
    """Class to connect to the Algolia API"""

    def __init__(self, app_id: Text, search_key: Text, index: Text):
        self.client = SearchClient.create(app_id, search_key)
        self.index = self.client.init_index(index)

    def get_algolia_link(self, hits: List, index: int):
        doc_link = f"- [{hits[index].get('hierarchy').get('lvl0')}"
        if hits[index]["hierarchy"].get("lvl1"):
            doc_link += f"/{hits[index].get('hierarchy').get('lvl1').strip()}"
            if hits[index]["hierarchy"].get("lvl2"):
                doc_link += f"/{hits[index].get('hierarchy').get('lvl2').strip()}"
        doc_link += f"]({hits[index].get('url')})"
        return doc_link

    def search(self, search_string: Text):
        res = self.index.search(search_string)
        return res
