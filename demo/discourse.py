import requests
from typing import Text

class DiscourseAPI(object):
    """Class to connect to the Algolia API"""

    def __init__(self, url: Text):
        self.url = url

    def get_discourse_links(self, topics: [Text], index: int):
        doc_url = f"https://forum.rasa.com/t/{topics[index]['slug']}/{str(topics[index]['id'])}"
        forum = f"- [{topics[index]['title']}]({doc_url})"
        return forum

    def query(self, search_string: Text, include_blurbs=False):
        params = {'term': search_string, 'include_blurbs': include_blurbs}
        res = requests.get(url=f"{self.url}/query.json", params=params)
        return res

    def search(self, search_string: Text, include_blurbs=False):
        params = {'q': search_string}
        headers={"Content-Type":"application/json; charset=utf-8"}
        res = requests.get(url=self.url, params=params, headers=headers)
        return res
