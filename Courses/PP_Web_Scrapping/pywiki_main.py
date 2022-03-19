import scrapy
from scrapy.crawler import CrawlerProcess


class PyWiki(scrapy.Spider):

    name = "pywiki"

    # this method yields a scrapy response object to a parsing function for processing
    def start_requests(self):
        site_url = 'https://en.wikipedia.org/wiki/Python'
        yield scrapy.Request(url=site_url, callback=self.parse) # this callback needs to match the parse function we define

    # scraping magic happens here
    def parse(self, response):
        # write out HTML
        html_file = 'pywiki.html'
        with open(html_file, 'wb') as html_out:
            html_out.write(response.body)


# Run process
process =  CrawlerProcess()
process.crawl(PyWiki)
process.start()