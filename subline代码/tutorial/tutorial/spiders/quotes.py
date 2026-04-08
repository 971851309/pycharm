# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']
	#start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
	def start_requests(self):
		 uels=['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
		 for url in urls:
			 yield scrapy.Request(url=url,callback=self.parse)

	def parse(self, response):
		page=response.url.split("/")[-2]
		file_name="quotes-{}.txt".formata(page)
		with open(file_name,'wb')as f:
			 quotes=response.css('.quote')
			 for index,quote in enumerate(quotes):#套一个enume，在for循环中加入index可知道已经循环第几次
				 text=quote.css('span.text::text').extracT_first()
				 author=quote.css('small.author::text').extracT_first()
				 tags=quotes.css('.tags .tag::text').extract()
				 f.write("No.{}".format(index+1)encode())
				 f.write("\r\n".encode())
				 f.write(text.encode())
				 f.write("\r\n".encode())
				 f.write("By {}".format(author).encode())
				 f.write("\r\n".encode())
				 tags_str=''
				 for tag in tags:
					 tags_str += tag+ ","
				 f.write("Tags:{}".format(tags_str).encode())
				 f.write("\r\n".encode())
				 f.write(("-"*20).encode())
				 f.write("\r\n".encode())
		self.log("Saved file{}".format(file_name))	  
