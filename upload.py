""" Daemon for webscraping comics news sites """
import json
import logging
import logging.config
import os
import sys

from config import db, schema, sentry
from scrapers import (BleedingCool, Cbr, Comicbook, Comicsbeat, Ign, Nerdist,
                      Newsarama, Outhousers)

def setup_logging(
        default_path='configs/logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
    ):
    """ Setup logging configuration """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize constants
with open('configs/sources.json') as f:
    data = f.read()
    sites = json.loads(data)


def get_scraper(src: str):
    """Summary:
            This function is a 'switch' so that executes the webscraping functions for each source.

    Args:
            src (String): Webscraping Source

    Returns:
            instance: Webscraping Class.
    """

    switcher = {
        'bleedingcool': BleedingCool(),
        'cbr': Cbr(),
        'comicbook': Comicbook(),
        'comicsbeat': Comicsbeat(),
        'ign': Ign(),
        'nerdist': Nerdist(),
        'newsarama': Newsarama(),
        'outhousers': Outhousers(),
    }
    return switcher.get(src, "Invalid Source")


def scraper(src: str, reset=False) -> None:
    """Summary
            Scrapes website according to source and uploads scraped data to database.
    Args:
            src (String): Webscraping Source
    """
    try:
        logger.info(f'Beginning Scrape of {src}.')
        site = get_scraper(src)
        logger.info(f'Ending Scrape of {src}.')

        # Get website data
        data = site.scrape()

        if reset:
            logger.info(f'Reset {src} table')
            schema.drop(src)
            with schema.create(src) as table:
                table.string("title")
                table.string("link")

        # Clear out old info
        db.table(src).truncate()

        logger.info(f'Uploading {src} data.')
        db.table(src).insert(data)
        logger.info(f'Uploading of {src} data completed.')
    except Exception as e:
        logger.exception(e)
        sentry.capture_exception()
        pass

if __name__ == '__main__':

    # Upload Sources
    logger.info('Webscraper Starting up')

    # Where the magic happens! Scrapes via web source
    for src in sites["sources"]: scraper(src)    
        
    logger.info('Webscraper Finished')

