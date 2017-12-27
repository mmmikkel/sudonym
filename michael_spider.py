import scrapy
import re

class QuotesSpider(scrapy.Spider):
	name = "michaelemail"
	start_urls = [
		'https://michael.duyvesteijn.net/',
	]

	def parse(self, response):
		privacyLink = response.xpath('//li/a[re:test(@href,".*how.*")]/@href').extract_first()
		if privacyLink is not None:
			yield response.follow(privacyLink, callback=self.parse1)

	def parse1(self, response):

 		m = response.css('h1::text').re(r'.*')

 		#This below all works
		#privacy = response.css('li a::text').re(r'How.*')
		#privacy = response.css('li.page_item.page-item-17 a::attr(href)').extract_first()
		#privacy2 = response.xpath('//li/a/text()').extract_first()
		#privacy2 = response.xpath('//li/a/text()').re(r'How.*')
		#privacy2 = response.xpath('//li/a[re:test(@href,".*how.*")]/@href').extract_first()


		#divs = response.xpath('//div')
		#for a in divs.xpath('.//a[re:test(@href, "(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)")]/@href'):  # extracts all <p> inside
		#for a in divs.xpath('.//p[re:test(text(), ".*Operations.*")]/text()'):
		divs = response.xpath('//div/p[re:test(text(), ".*Operations.*")]/text()')
		#divs.xpath('.//a[re:test(@href, "(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)")]/@href')  # extracts all <p> inside

		yield {
		    'href': divs.extract(),
		    'm': m,
		    #'privacy': privacy,
		    #'privacy2':privacy2,
		}