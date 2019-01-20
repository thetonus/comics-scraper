""" Daemon for webscraping comics news sites """
import json
import logging
import logging.config
import os
import sys

import sentry_sdk

from config import db, schema, sentry
from scrapers import ScraperFactory

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


def scraper(src: str) -> None:
    """Summary
            Scrapes website according to source and uploads scraped data to database.
    Args:
            src (String): Webscraping Source
    """
    try:
        logger.info(f'Beginning Scrape of {src}.')
        site = ScraperFactory().make(src)
        logger.info(f'Ending Scrape of {src}.')

        # Get website data
        data = site.scrape()

        # Clear out old info
        db.table(src).truncate()

        logger.info(f'Uploading {src} data.')
        db.table(src).insert(data)
        logger.info(f'Uploading of {src} data completed.')
    except Exception as e:
        logger.exception(e)
        sentry_sdk.capture_exception()
        pass


if __name__ == '__main__':

    # Upload Sources
    logger.info('Webscraper Starting up')

    # Where the magic happens! Scrapes via web source
    for src in sites["sources"]:
        scraper(src)

    logger.info('Webscraper Finished')
