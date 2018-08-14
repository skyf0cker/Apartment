import scrapy
from scrapy import Selector
from FirstBlood.items import FirstbloodItem


class Apartment(scrapy.Spider):

	name = "Apartment"

	allow_domains = ["zu.taiyuan.fang.com"]

	start_urls = ["http://zu.taiyuan.fang.com"]

	name_list = []

	addr_list = []

	price_list = []

	squ_list = []

	def parse(self, response):

		fb = FirstbloodItem()

		s = Selector(response)
		target_url = s.xpath('//*[@id="rentid_D10_01"]/a[7]/@href').extract()
		target_url = "http://zu.taiyuan.fang.com" + target_url[0]
		if len(target_url) != 0:
			for i in range(30):
				try:
					fb['name'] = s.xpath('//*[@id="listBox"]/div[2]/dl['+str(i+1)+']/dd/p[@class="title"]/a/text()').extract()
					fb['address'] = ''.join(s.xpath('//*[@id="listBox"]/div[2]/dl['+str(i+1)+']/dd/p[@class="gray6 mt20"]/a/span/text()').extract())
					fb['price'] = s.xpath('//*[@id="listBox"]/div[2]/dl['+str(i+1)+']/dd/div[@class="moreInfo"]/p/span/text()').extract()
					fb['square'] = s.xpath('//*[@id="listBox"]/div[2]/dl['+str(i+1)+']/dd/p[2]/text()[3]').extract()
					yield fb
				except:
					continue
			yield scrapy.Request(target_url, callback= self.parse)






		# 	target_url = "http://zu.taiyuan.fang.com" + target_url[0]
		# 	self.name_list.extend(s.xpath('//*[@id="listBox"]/div[2]/dl/dd/p[@class="title"]/a/text()').extract())
		# 	self.addr_list.extend(s.xpath('//*[@id="listBox"]/div[2]/dl/dd/p[@class="gray6 mt20"]/a/text()').extract())
		# 	self.price_list.extend(s.xpath('//*[@id="listBox"]/div[2]/dl/dd/div[@class="moreInfo"]/p/span/text()').extract())
		# 	self.squ_list.extend(s.xpath('//*[@id="listBox"]/div[2]/dl/dd/p[2]/text()[3]').extract())
		# 	yield scrapy.Request(target_url, callback= self.parse)
		# else:
		# 	for name in self.name_list:
		# 		fb["name"] = name
		# 		print(name)
		# 		fb["address"] = "".join(self.addr_list[self.name_list.index(name)*3:self.name_list.index(name)*3+3])
		# 		print("".join(self.addr_list[self.name_list.index(name)*3:self.name_list.index(name)*3+3]))
		# 		fb["square"] = self.squ_list[self.name_list.index(name)]
		# 		print(self.squ_list[self.name_list.index(name)])
		# 		fb["price"] = self.price_list[self.name_list.index(name)]
		# 		print(self.price_list[self.name_list.index(name)])
		# 		yield fb
			




