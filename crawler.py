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
		"""Constructor: words can be split with ';', or from a list."""
		if isinstance(words, list):
			self.keywords = words
		else:
			self.keywords = words.split(';')
	
	def run(self):
		"""Main entrance"""
		for keyword in self.keywords:
			keyword = keyword.strip()
			if keyword == '':
				continue
			file_handler = open('data/'+'_'.join(keyword.split())+'.txt', 'w+')
			file_handler.write('********************************************************************\n')
			file_handler.write('Keyword: '+keyword+'\n')
			search_entity = SearchItemListEntity(keyword)
			search_entity.getItems()
			for item in search_entity.itemlist:
				file_handler.write('-------------------------------------------------------------------\n')
				file_handler.write('Item name: '+item['name']+'\n')
				offer_entity = ItemOfferListEntity(item['asin'])
				offer_entity.getOffers()
				for offer in offer_entity.offerlist: 
					file_handler.write(offer+'\n')
			file_handler.close()


if __name__ == '__main__':
	words = open('searchlist.txt', 'r').readlines()
	crawler = Crawler(words)
	crawler.run()
