""" Scraper Factory """

from scrapers import (BleedingCool, Cbr, Comicbook, Comicsbeat, Ign, Nerdist,
                      Newsarama, Outhousers)


class ScraperFactory:

    scrapers = {'bleedingcool': BleedingCool,
                'cbr': Cbr,
                'comicbook': Comicbook,
                'comicsbeat': Comicsbeat,
                'ign': Ign,
                'nerdist': Nerdist,
                'newsarama': Newsarama,
                'outhousers': Outhousers}

    def make(self, source):
        """ Return Scraper """
        return self.scrapers[source]()
