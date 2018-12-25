""" Main Webscrape Application
"""
import pandas as pd

# Webscrapers
from .scrapers import (BleedingCool,
                       Cbr,
                       Comicbook,
                       Comicsbeat,
                       Ign,
                       Nerdist,
                       Newsarama,
                       Outhousers)

from helpers.sentry import client
from .sources import sources  # Webscraping Sources
from settings import db


def webscrape_functions(src: str):
    """Summary:
            This function is a 'switch' so that executes the webscraping functions for each source.

    Args:
            src (String): Webscraping Source

    Returns:
            Function: Webscraping function for specific source.
    """

    switcher = {
        'bleedingcool': BleedingCool,
        'cbr': Cbr,
        'comicbook': Comicbook,
        'comicsbeat': Comicsbeat,
        'ign': Ign,
        'nerdist': Nerdist,
        'newsarama': Newsarama,
        'outhousers': Outhousers,
    }
    return switcher.get(src, "Invalid Source")


def scraper(src: str, log) -> None:
    """Summary
            Scrapes website according to source and uploads scraped data to database.
    Args:
            src (String): Webscraping Source
            engine (DB Engine): DB engine
            log (log): Logger
    """
    try:
        log.info(f'Beginning Scrape of {src}.')
        Site = webscrape_functions(src)
        log.info(f'Ending Scrape of {src}.')
        # log.debug(data())
        site = Site()
        data = site.scraper()
        
        log.info(f'Uploading {src} data.')
        db.table(src).truncate()
        db.table(src).insert(data)
        log.info(f'Uploading of {src} data completed.')
    except ValueError as e:
        log.critical(e)
        client.capture_exception()
        pass
    except Exception as e:
        log.critical(e)
        client.capture_exception()
        pass


def run(log) -> None:
    """Summary:
            Scrapes all the data for each source. Main function for webscraping service.

    Args:
            src (String): Webscraping Source
            log (log): Logger
    """

    # Where the magic happens! Scrapes via web source
    for src in sources:
        scraper(src, log)

    log.info('Total webscraping complete. ')
   