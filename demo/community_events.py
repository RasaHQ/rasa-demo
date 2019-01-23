import ssl
from typing import List, Optional, Text
import logging

logger = logging.getLogger(__name__)


class CommunityEvent(object):

    def __init__(self, name, city, country, date, link):
        self.name = name
        self.city = city
        self.country = country
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

        city, name, date_as_string = html.get_text().split(',')
        country = get_country_for(city)

        date_format = '%d %B %Y'
        date = datetime.strptime(date_as_string.strip(), date_format)

        return cls(name.strip(), city.strip(), country, date, link.strip())

    def formatted_date(self):
        return self.date.strftime("%B %d, %Y")

    def name_as_link(self):
        return "[{}]({})".format(self.name, self.link)

    def as_kwargs(self):
        return {'event_name': self.name_as_link(),
                'event_location': self.city,
                'event_date': self.formatted_date()}


def get_community_events() -> List[CommunityEvent]:
    """Returns list of community events sorted ascending by their date."""
    from bs4 import BeautifulSoup
    import requests as r
    from datetime import datetime

    response = r.get('https://rasa.com/community/join/')

    if response.status_code == 200:
        community_page = response.content

        soup = BeautifulSoup(community_page, 'html.parser')

        events = soup.find('ul', attrs={'class': 'bulleted'}).find_all('li')
        events = [CommunityEvent.from_html(e) for e in events]

        now = datetime.now()
        events = [e for e in events if e is not None and e.date > now]

        return sorted(events, key=lambda e: e.date)

    return []


def get_country_for(city: Text) -> Optional[Text]:
    from geopy.geocoders import Nominatim
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    geo_locator = Nominatim(ssl_context=ssl_context)
    location = geo_locator.geocode(city, language='en', addressdetails=True)

    if location:
        return location.raw['address'].get('country')

    return None
