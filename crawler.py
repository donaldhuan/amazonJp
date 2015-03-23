# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup as bs
import os
#------
from settings import *
from entity.SearchItemListEntity import SearchItemListEntity
from entity.ItemOfferListEntity import ItemOfferListEntity 

class Crawler:
	def __init__(self, words):
		self.keywords = words
 

if __name__ == '__main__':
	#searcher = SearchItemListEntity('iphone 6')
	#searcher.getItems()
	#print len(searcher.itemlist)
	#print searcher.itemlist
	offer = ItemOfferListEntity('B003UIRICC')
	offer.getOffers()
	print len(offer.offerlist)
	print offer.offerlist
