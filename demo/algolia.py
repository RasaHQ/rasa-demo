# -*- coding: utf-8 -*-
from algoliasearch.search_client import SearchClient

class AlgoliaAPI(object):
    """Class to connect to the Algolia API"""

    def __init__(self, app_id, search_key, index):

        self.client = SearchClient.create(app_id, search_key)
        self.index = self.client.init_index(index)

    def search(self, search_string):
        res = self.index.search(search_string)
        return res


