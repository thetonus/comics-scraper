"""Summary: Webscraper for cbr.com
"""
from typing import Dict, List, Tuple

import requests
from bs4 import BeautifulSoup

from .BaseScraper import BaseScraper


class Cbr(BaseScraper):

    def __init__(self):
        super().__init__()
        self.urls = [
            'https://www.cbr.com/category/comics/news/page/{}'.format(i) for i in range(1, 3)]

    def _raw_scrape(self, url: str):
        """Summary:
            Gets the raw data from site.

        Args:
            url (String): url for site
            headers (string): headers for bs4 to tell site it is a legitimate browser

        Returns:
            bs4: Raw scraped data
        """

        r = requests.get(url, headers=self._headers)

        soup = BeautifulSoup(r.content, "lxml")
        entries = soup.find_all('a')
        return entries

    @staticmethod
    def _extract_content(entries) -> Tuple[List[str], List[str]]:
        """Summary:
            Extracts titles and links from raw data
        Args:
            entries (bs4): Raw scraped data

        Returns:
            list: Scraped and cleaned article titles and links
        """
        titles = list()
        links = list()
        for entry in entries:
            titles.append(entry.text), links.append(entry.attrs['href'])

        titles = list(filter(None.__ne__, titles))
        links = list(filter(None.__ne__, links))
        return titles, links

    def scrape(self):
        """Summary:
            Main webscraper function

        Returns:
            dict: dictionary output for Pandas DataFrame
        """

        titles, links = list(), list()

        for url in self.urls:
            entries = self._raw_scrape(url)
            titles_temp, links_temp = self._extract_content(entries)
            titles.extend(titles_temp), links.extend(links_temp)

        template = "https://www.cbr.com"
        return self._dict_output(titles, links, template=template)
