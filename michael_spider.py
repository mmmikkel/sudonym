import scrapy


class QuotesSpider(scrapy.Spider):
    name = "michaelemail"
    start_urls = [
        'https://michael.duyvesteijn.net',
    ]

    def parse(self, response):
        for michaelemail in response.css('div.textwidget'):
            yield {
                'mail': michaelemail.css('a::attr("href")').extract_first(),
            }