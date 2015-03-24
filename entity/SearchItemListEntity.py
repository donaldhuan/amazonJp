import urllib2
from bs4 import BeautifulSoup as bs
#------
import settings
import util

class SearchItemListEntity:
	"""Get items after inputting a keyword into the searching field."""

	def __init__(self, word):
		"""Constructor"""
		self.keyword = '+'.join(word.split())
		self.url = settings.baseUrl + settings.searchPostfix \
				+ self.keyword
		self.itemlist = []
	
	def createBSObj(self, page=1):
		"""Different pages, different BeautifulSoup instances."""
		url = self.url+'&page='+str(page)
		bsObj = bs(util.getDecodedHtml(url), 'lxml')
		return bsObj

	def pageProcess(self, bsObj):
		"""Parsing html content, get target data."""
		li_res = bsObj.select('#atfResults > ul > li')
		items = []
		for li in li_res:
			items.append(li.attrs['data-asin'])
		return items

	def getPageNumsAndParseFirstPage(self):
		"""From first page, get the total page number; 
		meanwhile parse this page."""
		bsObj = self.createBSObj()

		#get items from first page
		self.itemlist = self.itemlist + self.pageProcess(bsObj)

		#get number of searching list
		div_pagn = bsObj.find('div', id='pagn')
		span_pagnRA = div_pagn.select('span.pagnRA')
		if (len(span_pagnRA) == 0):
			return 1
		else:
			return int(span_pagnRA[0].find_previous('span').text)
	

	def getItemsByPage(self, page):
		"""Get items from a specific page."""
		bsObj = self.createBSObj(page)
		return self.pageProcess(bsObj)
	
	def getItems(self):
		"""Get items of a keyword searching."""
		pageNums = self.getPageNumsAndParseFirstPage()
		for i in range(1, pageNums):
			self.itemlist = self.itemlist + self.getItemsByPage(i+1)
