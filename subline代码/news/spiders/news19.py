# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import NewsItem

class News19Spider(CrawlSpider):
	name = 'news19'
	allowed_domains = ['news.163.com']
	start_urls = ['http://news.163.com/']

	rules = (
		Rule(LinkExtractor(allow=r'http://news.163.com/20/0115/\d+/.*?\.'), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		item=NewsItem()
		#item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
		#item['name'] = response.xpath('//div[@id="name"]').get()
		#item['description'] = response.xpath('//div[@id="description"]').get()
		item['news_thread']=response.url.strip().split('/')[-1][:-5]#strip,用于去除前后端的空白,split用于分割
		self.get_title(response,item)
		self.get_time(response,item)
		self.get_source(response,item)
		self.get_body(response,item)
		self.get_source_url(response,item)
		self.get_url(response,item)
		return item
	def get_title(self,response,item):
		title=response.css('.post_content_main h1::text').extract()
		if title:
			print('title:{}'.format(title[0][:-5]))
			item['news_title']=title[0][:-5]
	def get_time(self,response,item):
		time=response.css('div.post_time_source::text').extract()		
		if time:
			print("time:{}".format(time[0].strip().replace()))
			item['news_time']=time[0].strip().replace()
	def get_source(self,response,item):
		source=response.css('post_time_source').extract()	
		if source:
			source['news_source']=source[0]
	def get_body(self,responce,item):
		title=post_body.css('div.post_body::text').extract()
		if body:
			item['news_body']=body
	def get_source_url(self,responce,item):
		get_source_url=response.css('post_time_source::attr(href').extract()
		if source_url:
			item['source_url']=source_url[0]
	def get_url(self,responce,item):
		url=response.url
		if url:
			item['news_url']=url