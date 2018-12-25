"""Summary: Webscraper for outhouses.com
"""
from typing import Dict, List, Tuple

import requests
from bs4 import BeautifulSoup

from .BaseScraper import BaseScraper


class Outhousers(BaseScraper):

    def __init__(self):
        super().__init__()
        self.url = 'http://www.theouthousers.com/index.php/news.html'

    def _raw_scrape(self):
        """Summary:
            Gets the raw data from site.

        Args:
            url (String): url for site
            headers (string): headers for bs4 to tell site it is a legitimate browser

        Returns:
            bs4: Raw scraped data
        """
        r = requests.get(self.url, headers=self._headers)

        soup = BeautifulSoup(r.content, "lxml")
        entries = soup.find_all('h4', {'class': 'media-heading'})
        return entries

    @staticmethod
    def _extract_content(entries):
        """Summary:
            Extracts titles and links from raw data
        Args:
            entries (bs4): Raw scraped data

        Returns:
            list: Scraped and cleaned article titles and links
        """
        titles, links = list(), list()

        for article in entries:
            anchors = article.find_all("a")
            for tag in anchors:
                titles.append(tag.text), links.append(tag['href'])

        titles = list(filter(None.__ne__, titles))
        links = list(filter(None.__ne__, links))
        return titles, links

    def scrape(self):
        """Summary:
            Main webscraper function

        Returns:
            dict: dictionary output for Pandas DataFrame
        """
        template = 'http://www.theouthousers.com'
        entries = self._raw_scrape()
        titles, links = self._extract_content(entries)
        return self._dict_output(titles, links, template=template)
