# Comic News Scraper

This project scrapes comic news websites and uploads the scraped contents to my Postgres DB every hour. This content is seen at my site [tonyhammack.com/comics](http://tonyhammack.com/comics)

## Webscraping Sources
My sources are: bleedingcool.com, cbr.com, comicbook.com, comicsbeat.com, ign.com, nerdist.com, newsarama.com, and theouthousers.com.

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

Here are the prerequisite modules used in this application.
```
orator
bs4
```

### Installing the conventional way


Install dependencies

```
pip3 install -r requirements.txt
```
In your `.env` file, enter your Sentry api key, your Postgres Database credentials, and Discord webhook information. In config.py, change the rss feeds and database tables to yours.

## Start Application

Initiate daemon
```
python3 upload.py
```

## Built With

* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Webscraping software
* [Orator](https://orator-orm.com/) - Active Record ORM

## Authors

* **[Tony Hammack](https://github.com/hammacktony/)**


## License

This project is licensed under the MIT License - see the 
[LICENSE.md](LICENSE.md) file for details
