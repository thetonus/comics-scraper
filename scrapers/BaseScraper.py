""" Archetype for Webscrapers """
import json
import os
from abc import ABC, abstractmethod

import validators

ROOT_DIR = os.getcwd()  # This is your Project Root


class BaseScraper(ABC):
    """ Base Sraper """

    def __init__(self):
        # Get search Criterion
        with open(f'{ROOT_DIR}/configs/criterion.json') as f:
            data = f.read()
            criterion = json.loads(data)
        self._criterion = set(map(str.lower, criterion["criterion"]))

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
                    found_titles.append(
                        title.strip()), found_links.append(link.strip())
        
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
            data (Dict): dictionary of titles and links
        """

        data = list()
        filtered_titles, filtered_links = self._filter_content(titles, links)

        if template:

            # Return content with apping template to links
            filtered_links = list(map(lambda x: template + x, filtered_links))
            for i, (t, l) in enumerate(zip(filtered_titles, filtered_links)):
                data.append(dict())
                data[i]["title"] = str(t)
                data[i]["link"] = str(l)
            return data

        # Return content without adding template to links
        for i, (t, l) in enumerate(zip(filtered_titles, filtered_links)):
            data.append(dict())
            data[i]["title"] = str(t)
            data[i]["link"] = str(l)

        return data

    @abstractmethod
    def _raw_scrape(self):
        """ Placeholder for getting the RAW html from page """

    @abstractmethod
    def _extract_content(self):
        """ Extract text and links from RAW html """

    @abstractmethod
    def scrape(self):
        """ Run scraper """
