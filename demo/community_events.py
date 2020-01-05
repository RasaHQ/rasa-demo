import ssl
from datetime import datetime
from typing import Dict, List, Optional, Text
import logging

logger = logging.getLogger(__name__)

DATE_FORMAT = "%d %B, %Y"


class CommunityEvent:
    def __init__(self, name, city, country, formatted_date, date, link) -> None:
        self.name = name
        self.city = city
        self.country = country
        self.formatted_date = formatted_date
        self.date = date
        self.link = link

    def __repr__(self) -> Text:
        return "{} ({}): {} ({})".format(
            self.name, self.city, self.formatted_date, self.date
        )

    @classmethod
    def from_html(cls, html) -> Optional["CommunityEvent"]:
        try:
            city = html.contents[0]
            link = html.contents[3].get("href")
            name = html.contents[3].contents[0]
            date_as_string = html.contents[8]
            country = get_country_for(city)
            date = parse_community_date(date_as_string).date()
        except Exception as e:
            logger.warning(f"Error when trying to parse event details from html.\n{e}")
            return None

        return cls(
            name.strip(),
            city.strip(),
            country,
            date_as_string.strip(),
            date,
            link.strip(),
        )

    def name_as_link(self) -> Text:
        return "[{}]({})".format(self.name, self.link)

    def as_kwargs(self) -> Dict[Text, Text]:
        return {
            "event_name": self.name_as_link(),
            "event_location": self.city,
            "event_date": self.formatted_date,
        }


def parse_community_date(date_string: Text) -> datetime:

    dates = date_string.split("-")

    try:
        return datetime.strptime(dates[-1].strip(), DATE_FORMAT)
    except Exception as e:
        logger.warning(e)
        return datetime.min


def get_community_events() -> List[CommunityEvent]:
    """Returns list of community events sorted ascending by their date."""
    from bs4 import BeautifulSoup
    import requests as r
    import datetime

    response = r.get("https://rasa.com/community/join/")

    if response.status_code == 200:
        community_page = response.content

        soup = BeautifulSoup(community_page, "html.parser")

        events = soup.find("ul", attrs={"id": "events-list"}).find_all("li")
        # [1].find("ul").find_all("li")
        events = [CommunityEvent.from_html(e) for e in events]

        now = datetime.date.today()
        events = [e for e in events if e is not None and e.date >= now]
        return sorted(events, key=lambda e: e.date)

    return []


def get_country_for(city: Text) -> Optional[Text]:
    from geopy.geocoders import Nominatim

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    geo_locator = Nominatim(ssl_context=ssl_context)
    location = geo_locator.geocode(city, language="en", addressdetails=True)

    if location:
        return location.raw["address"].get("country")

    return None
