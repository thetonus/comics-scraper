"""Summary: Webscraper for bleedingcool.com
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Tuple, Dict
from .BaseScraper import BaseScraper

class BleedingCool(BaseScraper):

    def __init__(self):
        super().__init__()
        self.url = "https://www.bleedingcool.com/tag/dc/"

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
        for article in entries:
            cards = article.find_all("div", {'class': 'row white mini-card'})
            for card in cards:
                divs = card.find_all('div', {'class': 'col s9'})
                for div in divs:
                    headers = div.find_all(
                        'h2', {'class': 'card-title-smaller truncate-ellipsis'})
                    for header in headers:
                        titles.append(header.text)
                        links.append(article['href'])
                        
        titles = list(filter(None.__ne__, titles))
        links = list(filter(None.__ne__, links))
        return titles, links

    def scrape(self):
        """Summary:
            Main webscraper function

        Returns:
            dict: dictionary output for Pandas DataFrame
        """

        entries = self._raw_scrape()
        titles, links = self._extract_content(entries)

        return self._dict_output(titles, links)


