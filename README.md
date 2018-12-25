# Heroku Daemon

This is my daemon for [my heroku application](http://tonus.herokuapp.com). Currently it scrapes comic news websites and uploads the scraped contents to my Postgres DB every hour. The search criterion I used are in search_criterion.py. The daemon also searches the feeds of [thebatmanuniverse.com](http://thebatmanuniverse.com) for new posts. It these posts are then sent to a Discord Server.

## Webscraping Sources
My sources are: bleedingcool.com, cbr.com, comicbook.com, comicsbeat.com, ign.com, nerdist.com, newsarama.com, and theouthousers.com.

## TBU Discord Bot
TBU uses Discord to talk about comics with their audience. I realized that the editor in chief spent a long time manually cutting and pasting the articles of the site into specific Discord channels.
Since TBU is a Wordpress site, I wondered if there would be a way to took at the rss feeds and add new stories to the Discord server. The "discord_bot" allows the autoposting of new TBU content when
it is published on the site.

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
