# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup as bs
import os
#------
import settings
from entity.SearchItemListEntity import SearchItemListEntity
from entity.ItemOfferListEntity import ItemOfferListEntity 

class Crawler:
	"""A robot to scrapy data from amazon.co.jp with searching words."""

	def __init__(self, words):
		"""Constructor: words can be split with ';'."""
		self.keywords = words.split(';')
	
	def run(self):
		for keyword in self.keywords:
			file_handler = open('data/'+'_'.join(keyword.split()), 'w+')
			file_handler.write('********************************************************************\n')
			file_handler.write('Keyword: '+keyword+'\n')
			search_entity = SearchItemListEntity(keyword)
			search_entity.getItems()
			for item in search_entity.itemlist:
				file_handler.write('-------------------------------------------------------------------\n')
				file_handler.write(item+'\n')
				offer_entity = ItemOfferListEntity(item)
				offer_entity.getOffers()
				for offer in offer_entity.offerlist: 
					file_handler.write(offer+'\n')
			file_handler.close()


if __name__ == '__main__':
	#search_entity = SearchItemListEntity('iphone 6')
	#search_entity.getItems()
	#print search_entity.itemlist
	#offer_entity = ItemOfferListEntity('B003UIRICC')
	#offer_entity.getOffers()
	#print offer_entity.offerlist
	crawler = Crawler('ip ; oo')
	crawler.run()
