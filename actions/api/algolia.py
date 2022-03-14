# -*- coding: utf-8 -*-
from algoliasearch.search_client import SearchClient
from typing import Text, List

import spacy

en_spacy = spacy.load("en_core_web_md")

additional_stopwords = {"need", "want", "help", "able", "unable", "know", "use"}
STOPWORDS = spacy.lang.en.stop_words.STOP_WORDS.union(additional_stopwords)


def preprocess_search_text(search_text: Text) -> Text:
    tokens = en_spacy(search_text.lower())
    stripped_search_text = " ".join(
        [w.text for w in tokens if w.text not in STOPWORDS and not w.is_punct]
    )
    return stripped_search_text


class AlgoliaAPI(object):
    """Class to connect to the Algolia API"""

    def __init__(self, app_id: Text, search_key: Text, index: Text):
        self.client = SearchClient.create(app_id, search_key)
        self.index = self.client.init_index(index)

    def get_algolia_link(self, hits: List, index: int) -> Text:
        doc_link = f"- [{hits[index].get('hierarchy').get('lvl0')}"
        if hits[index].get("hierarchy").get("lvl1"):
            doc_link += f"/{hits[index].get('hierarchy').get('lvl1').strip()}"
            if hits[index].get("hierarchy").get("lvl2"):
                doc_link += f"/{hits[index].get('hierarchy').get('lvl2').strip()}"
        doc_link += f"]({hits[index].get('url')})"
        return doc_link

    def search(self, search_string: Text):
        search_text = preprocess_search_text(search_string)
        res = self.index.search(search_text)
        return res
