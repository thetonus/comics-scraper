""" Archetype for Webscrapers """
from abc import ABC, abstractmethod

import validators

from .criterion import criterion


class BaseScraper(ABC):
    """ Base Sraper """

    def __init__(self):
        self._criterion = set(map(str.lower, criterion))
        # self._criterion = criterion
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'}

    def _filter_content(self, titles, links):
        """Summary
            Filters each article title by search criterion and validates url.
            Uses OrderedSet to easily remove duplicates but maintain sequential order.
        Args:
            titles (List): List of article titles
            links (List): List of article links

        Returns:
            found_titles and found_links: Sorted and unique titles and links
        """
        found_titles, found_links = list(), list()
        for key in self._criterion:
            for title, link in zip(titles, links):
                if key in title.lower():
                    found_titles.append(title.strip()), found_links.append(link.strip())

        # Return Unique values
        return list(dict.fromkeys(found_titles)), list(dict.fromkeys(found_links))

    def _dict_output(self, titles, links, template: str = ""):
        """"Summary
            Return dictionary output for pandas DataFrame

        Args:
            titles (List): List of article titles
            links (List): List of article links
            template (Str): Url template if need

        Returns:
            data: Lost containing a dictionary of titles and links
        """

        data = dict()
        if template:
            # Return content with apping template to links
            links = list(map(lambda x: template + x, links))
            data['title'], data['link'] = self._filter_content(titles, links)
            return [data]

        # Return content without adding template to links
        data['title'], data['link'] = self._filter_content(titles, links)
        return [data]

    @abstractmethod
    def _raw_scrape(self):
        """ Placeholder for getting the RAW html from page """

    @abstractmethod
    def _extract_content(self):
        """ Extract text and links from RAW html """

    @abstractmethod
    def scrape(self):
        """ Run scraper """
