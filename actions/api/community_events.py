from __future__ import annotations  # for typing by enclosing class

import ssl
import datetime
from typing import Dict, List, Optional, Text
import logging
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

logger = logging.getLogger(__name__)

DATE_FORMAT = "%d %B, %Y"
COMMUNITY_EVENT_PAGE = "https://rasa.com/community/join/"


class CommunityEvent:
    def __init__(self, name, city, country, formatted_date, date, link) -> None:
        self.name = name
        self.city = city
        self.country = country
        self.formatted_date = formatted_date
        self.date = date
        self.link = link

    @classmethod
    def from_html(cls, html) -> Optional["CommunityEvent"]:
        try:
            city = html.contents[-1]
            link = html.contents[0].get("href")
            name = html.contents[0].contents[0]
            date_as_string = html.contents[3]
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

    def __repr__(self) -> Text:
        return f"{self.name} ({self.city}): {self.formatted_date} ({self.date})"

    def name_as_link(self) -> Text:
        return f"[{self.name}]({self.link})"

    def as_kwargs(self) -> Dict[Text, Text]:
        return {
            "event_name": self.name_as_link(),
            "event_location": self.city,
            "event_date": self.formatted_date,
        }


def parse_community_date(date_string: Text) -> datetime.datetime:
    """Parse string date as datetime object"""
    dates = date_string.split("-")

    try:
        return datetime.datetime.strptime(dates[-1].strip(), DATE_FORMAT)
    except Exception as e:
        logger.warning(e)
        return datetime.datetime.max  # if date can't be parsed assume event is future


def get_community_events() -> List["CommunityEvent"]:
    """Return list of community events sorted ascending by their date."""
    response = get_community_page()

    if response.status_code == 200:
        community_page = response.content

        soup = BeautifulSoup(community_page, "html.parser")
        potential_events = soup.find("ul", attrs={"id": "events-list"})
        if potential_events:
            events = potential_events.find_all("li")
        else:
            events = []

        parsed_events = [CommunityEvent.from_html(e) for e in events]

        now = datetime.date.today()
        upcoming_events = [e for e in parsed_events if e is not None and e.date >= now]
        return sorted(upcoming_events, key=lambda e: e.date)

    return []


def get_country_for(city: Text) -> Optional[Text]:
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    geo_locator = Nominatim(ssl_context=ssl_context, user_agent="rasa-demo")
    location = geo_locator.geocode(city, language="en", addressdetails=True)

    if location:
        return location.raw["address"].get("country")

    return None


def get_community_page() -> requests.Response:
    return requests.get(COMMUNITY_EVENT_PAGE)
