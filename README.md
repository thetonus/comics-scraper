# Heroku Daemon

This project scrapes comic news websites and uploads the scraped contents to my Postgres DB every hour.

## Webscraping Sources
My sources are: bleedingcool.com, cbr.com, comicbook.com, comicsbeat.com, ign.com, nerdist.com, newsarama.com, and theouthousers.com.

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

Here are the prerequisite modules used in this application.
```
pandas
bs4
logging
sqlalchemy
orderedset
```

### Installing the conventional way


Install dependencies

```
pip install -r requirements.txt
```
In your `.env` file, enter your Sentry api key, your Postgres Database credentials, and Discord webhook information. In settings.py, change the rss feeds and database tables to yours.

## Start Application

Initiate daemon
```
python daemon.py
```

## Built With

* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Webscraping software
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) - Used to manipulate data
* [orderedset](http://orderedset.readthedocs.io/en/latest/orderedset.html) - Used to easily eliminate duplicates but keep order so that the title and url have same index

## Authors

* **[Tony Hammack](https://github.com/hammacktony/)**


## License

This project is licensed under the MIT License - see the 
[LICENSE.md](LICENSE.md) file for details
