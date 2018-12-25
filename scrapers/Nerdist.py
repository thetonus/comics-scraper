"""Summary: Webscraper for nerdist.com
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Tuple, Dict
from .BaseScraper import BaseScraper

class Nerdist(BaseScraper):
    def __init__(self):
        super().__init__()
        self.url = 'https://nerdist.com/category/comics/'


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
        raw_titles = soup.find_all('span', {'class': 'list-item-main-title'})
        raw_links = soup.find_all('a', {'class': 'post'})
        return raw_titles, raw_links

    @staticmethod
    def _extract_content(raw_titles, raw_links):
        """Summary:
            Extracts titles and links from raw data
        Args:
            entries (bs4): Raw scraped data

        Returns:
            list: Scraped and cleaned article titles and links
        """
        titles, links = list(), list()
        for title, link in zip(raw_titles, raw_links):
            titles.append(title.text), links.append(link['href'])

        titles = list(filter(None.__ne__, titles))
        links = list(filter(None.__ne__, links))
        return titles, links


    def scrape(self):
        """Summary:
            Main webscraper function

        Returns:
            dict: dictionary output for Pandas DataFrame
        """

        raw_titles, raw_links = self._raw_scrape()
        titles, links = self._extract_content(raw_titles, raw_links)
        return self._dict_output(titles, links)
