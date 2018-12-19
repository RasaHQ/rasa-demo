from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class CommunityEvent(object):

    def __init__(self, name, location, date, link):
        self.name = name
        self.location = location
        self.date = date
        self.link = link

    @classmethod
    def from_html(cls, html) -> Optional['CommunityEvent']:
        from datetime import datetime
        link = html.a.get('href')

        event_properties = html.get_text().split(',')

        if len(event_properties) != 3:
            logger.warning("Error when trying to parse event "
                           "details from html.")
            return None

        location, name, date_as_string = html.get_text().split(',')

        date_format = '%d %B %Y'
        date = datetime.strptime(date_as_string.strip(), date_format)

        return cls(name.strip(), location.strip(), date, link.strip())

    def formatted_date(self):
        return self.date.strftime("%B %d, %Y")

    def name_as_link(self):
        return "[{}]({})".format(self.name, self.link)


def get_community_events() -> List[CommunityEvent]:
    """Returns list of community events sorted ascending by their date."""
    from bs4 import BeautifulSoup
    import requests as r

    response = r.get('https://rasa.com/community/join/')

    if response.status_code == 200:
        community_page = response.content

        soup = BeautifulSoup(community_page, 'html.parser')

        events = soup.find('ul', attrs={'class': 'bulleted'}).find_all('li')
        events = [CommunityEvent.from_html(e) for e in events]
        events = [e for e in events if e is not None]

        return sorted(events, key=lambda e: e.date)

    return []
