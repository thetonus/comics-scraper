""" Load .env file variabless """
import os

from orator import DatabaseManager, Model
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Sentry Information
SENTRY_CLIENT_KEY = os.getenv("SENTRY_CLIENT_KEY")

# Discord Information
DISCORD = {
    "NEWS_COMICS": {
        "WEBHOOK": os.getenv("NEWS_COMICS_WEBHOOK"),
        "FEED": "http://thebatmanuniverse.net/category/comic/comic-news/feed",
        "TABLE": "comicNews",
    },
    "NEWS_MOVIE": {
        "WEBHOOK": os.getenv("NEWS_MOVIE_WEBHOOK"),
        "FEED": "http://thebatmanuniverse.net/category/movie/movie-news/feed",
        "TABLE": "movieNews",
    },
    "NEWS_TV": {
        "WEBHOOK": os.getenv("NEWS_TV_WEBHOOK"),
        "FEED": "http://thebatmanuniverse.net/category/tv/tv-news/feed",
        "TABLE": "tvNews",
    },
    "NEWS_VIDEOGAMES": {
        "WEBHOOK": os.getenv("NEWS_VIDEOGAMES_WEBHOOK"),
        "FEED": "http://thebatmanuniverse.net/category/videogame/videogame-news/feed",
        "TABLE": "gamesNews",
    },
    "NEWS_MERCH": {
        "WEBHOOK": os.getenv("NEWS_MERCH_WEBHOOK"),
        "FEED": "http://thebatmanuniverse.net/category/merchandise/merchandise-news/feed",
        "TABLE": "merchNews",
    },
    "NEWS_GENERAL": {
        "WEBHOOK": os.getenv("NEWS_GENERAL_WEBHOOK"),
        "FEED": "http://thebatmanuniverse.net/category/general/general-news/feed",
        "TABLE": "generalNews",
    },
    "PODCAST_COMICS": {
        "WEBHOOK": os.getenv("PODCAST_COMICS_WEBHOOK"),
        "FEED": "http://thebatmanuniverse.net/category/podcast/tbucp/feed",
        "TABLE": "comicsPodcast",
    },
}

# Database information
DATABASE={
    "default": {
        "driver": "postgres",
        "host": os.getenv("POSTGRES_HOST"),
        "database": os.getenv("POSTGRES_DB_NAME"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        'prefix': ''
    }
}

# Creates Base Orator Model
db = DatabaseManager(DATABASE)
