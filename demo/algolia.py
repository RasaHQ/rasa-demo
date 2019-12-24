# -*- coding: utf-8 -*-
from algoliasearch.search_client import SearchClient

class AlgoliaAPI(object):
    """Class to connect to the Algolia API"""

    def __init__(self, app_id, search_key, index):
        self.client = SearchClient.create(app_id, search_key)
        self.index = self.client.init_index(index)


    def get_algolia_link(self, hits, index: int):
        doc_link = f"- [{hits[index]['hierarchy']['lvl0']}"
        if hits[index]['hierarchy']['lvl1']:
            doc_link += f"/{hits[index]['hierarchy']['lvl1'].strip()}"
            if hits[index]['hierarchy']['lvl2']:
                doc_link += f"/{hits[index]['hierarchy']['lvl2'].strip()}"
        doc_link += f"]({hits[index]['url']})"
        return doc_link

    def search(self, search_string):
        res = self.index.search(search_string)
        return res


