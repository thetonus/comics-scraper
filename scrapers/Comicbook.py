"""Summary: Webscraper for comicbook.com
"""
import requests
from bs4 import BeautifulSoup
from .BaseScraper import BaseScraper

class Comicbook(BaseScraper):

    def __init__(self):
        super().__init__()
        self.urls = [
            'http://comicbook.com/comics/news?Page={}'.format(i) for i in range(1, 4)]

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
        entries = soup.find_all('div', {'class': 'headline-box'})
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
            headlines = entry.find_all('h1')
            for headline in headlines:
                articles = headline.find_all('a')
                for article in articles:
                    titles.append(article.text), links.append(article['href'])

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

        return self._dict_output(titles, links)



