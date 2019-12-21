# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)

class DiscourseAPI(object):
    """Class to connect to the Algolia API"""

    def __init__(self, url):
        self.url = url

    def get_discourse_links(self, stopics, index: int):
        doc_url = f"https://forum.rasa.com/t/{topics[index]['slug']}/{str(topics[index]['id'])}"
        forum = f"- [{topics[index]['title']}]({doc_url})"
        return forum

    def query(self, search_string, include_blurbs=False):
        import requests as r

        params = {'term': search_string, 'include_blurbs': include_blurbs}
        print(f"query params: {params}, url: {self.url}")
        res = r.get(url=self.url+"/query.json", params=params)
        return res

    def search(self, search_string, include_blurbs=False):
        import requests as r

        params = {'q': search_string}
        headers={"Content-Type":"application/json; charset=utf-8"}
        print(f"search params: {params}, url: {self.url}")
        res = r.get(url=self.url, params=params, headers=headers)
        return res
