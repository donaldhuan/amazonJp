# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup as bs
import os
#------
from settings import *
from entity.SearchItemListEntity import SearchItemListEntity

class Crawler:
	def __init__(self, words):
		self.keywords = words
 

if __name__ == '__main__':
	searcher = SearchItemListEntity('dsdディスク')
	searcher.getItems()
	print searcher.itemlist
