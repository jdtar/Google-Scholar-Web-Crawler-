### IMPORTANT ###
# In terminal use the command "scrapy crawl gsscraper"
# To output the file, add the command "-o 'filename'.csv"
# ex. scrapy crawl gsscraper -o "filename".csv

import scrapy
#import re
#import json
#from scrapy.crawler import CrawlerProcess
from gsscraper.items import GsscraperItem
#from scrapy.loader import ItemLoader
from scrapy.selector import Selector


### for not getting kicked off... spent 2 hours before realizing that you can turn off the damn robots.txt=True in the settings

###Find a different way of getting raw input and inserting that into the google scholar search terms...
###something something while loop where user can exit out or something. Probably find a way to enter all the terms at once and
###insert into a list and add them all into the start_url section



## fixed input with while loop
s = raw_input("Enter search terms: ")
list = map(str, s.split())
x = ''
y = 0 

while y < len(list):
    x +="+"+list[y]
    y+= 1


class googlescholarscraper(scrapy.Spider):
    name = "gsscraper"

    start_urls = [
        ### Cheesey ass way of searching through first four pages of results. Gotta change this shit later...
        ###keeping the first four pages of results. If more results wanted, after 'https://scholar.google.com/scholar?' add 'start=x&q=' where x is a multiple of 10. ex. 40 for 5th page, 50 for 6th page. 
        
        'https://scholar.google.com/scholar?hl=en&q='+x,
        'https://scholar.google.com/scholar?start=10&q='+x,
        'https://scholar.google.com/scholar?start=20&q='+x,
        'https://scholar.google.com/scholar?start=30&q='+x,            
    ]

    #parsing data the crawler looks for inside the html for each page... i think
    def parse(self, response):
        #for gs_r in response.xpath('//div[@class="gs_ri"]'):
        sel = Selector(response)
        item = GsscraperItem()

        url = sel.xpath('//h3[@class="gs_rt"]/a')
        titles = sel.xpath('//h3[@class="gs_rt"]/a')
        NumCited = sel.xpath('//div[@class="gs_fl"]/a[1]')
        Authors = sel.xpath('//div[@class="gs_a"]')
        Abstract = sel.xpath('//div[@class="gs_rs"]')

        #cleans data into readable text
        for a,b,c,d,e in zip(titles, NumCited, url, Authors, Abstract):
            title = a.xpath('.//text()').extract()
            ti = "".join(title)
            nc = b.xpath('.//text()'). extract()
            urls = c.xpath('./@href').extract()
            author = d.xpath('.//text()').extract()
            au = "".join(author)
            ab = e.xpath('.//text()').extract()
            abst = " ".join(ab)

            #outputs data
            yield {
                'Title' : ti,
                'NumCited' : nc,
                'URL' : urls,
                'Author, Year, Source Information': au,
                'Abstract' : abst,               
                }


            
            
            
##process = CrawlerProcess({
##    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
##})
##
##process.crawl(googlescholarscraper)
##process.start()



