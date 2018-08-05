# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GsscraperItem(scrapy.Item):
    URL = scrapy.Field()       # link to the article
    Title = scrapy.Field()     # title of the publication
    Authors = scrapy.Field()   # authors (example: DF Easton, DT Bishop, D Ford)
    Journal= scrapy.Field()   # journal name & year (example: Nature)
    Year = scrapy.Field()
    Publisher = scrapy.Field()    # journal Publisher 
    Abstract = scrapy.Field()  # abstract of the publication
    NumCited   = scrapy.Field() # number of times the publication is cited
    Terms = scrapy.Field()     # list of search terms used in the query
