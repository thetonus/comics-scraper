""" Load .env file variabless """
import os

import sentry_sdk
from dotenv import load_dotenv
from orator import DatabaseManager, Schema

# Load Environment
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Sentry Information and API
SENTRY_CLIENT_KEY = os.getenv("SENTRY_CLIENT_KEY")
sentry = sentry_sdk.init(SENTRY_CLIENT_KEY)

# Database information
DATABASE = {
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
schema = Schema(db)
