"""Summary: Webscraper for ign.com
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Tuple, Dict
from .BaseScraper import BaseScraper

class Ign(BaseScraper):

    def __init__(self):
        super().__init__()
        self.url = 'http://www.ign.com/comics'

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
        entries = soup.find_all('div', {'class': 'item-details'})
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

        for entry in entries:
            articles = entry.find_all('a', {'class': 'anchor'})
            for article in articles:
                titles.append(article.text), links.append(article['href'])

        titles = list(filter(None.__ne__, titles))
        links = list(filter(None.__ne__, links))
        return titles, links


    def scrape(self) -> Dict[List[str], List[str]]:
        """Summary:
            Main webscraper function

        Returns:
            dict: dictionary output for Pandas DataFrame
        """
    
        template = "http://www.ign.com"
        entries = self._raw_scrape()
        titles, links = self._extract_content(entries)
        return self._dict_output(titles, links, template=template)

