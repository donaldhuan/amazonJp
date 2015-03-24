# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup as bs
#------
import settings
import util

class ItemOfferListEntity:
	"""Get offers(shops that sell a item) of a specific item(with unique asin number)."""

	def __init__(self, asin):
		"""Constructor"""
		self.url = settings.baseUrl + settings.offerPostfix + asin + '/'
		self.offerlist = []

	def createBSObj(self, page=1):
		"""Different pages, different BeautifulSoup instances."""
		url = self.url+'?startIndex='+str(10*(page-1))
		bsObj = bs(util.getDecodedHtml(url), 'lxml')
		return bsObj

	def pageProcess(self, bsObj):
		"""Parsing html content, get target data."""
		div_olpOffer = bsObj.select('div.olpOffer')
		offers = []
		for offer in div_olpOffer:
			div_seller = offer.select('div.olpSellerColumn')[0]
			try:
				link = div_seller.select('a')[0].attrs['href']
				if (link[0] == '/'):
					#relative url
					link = settings.baseUrl + link
			except:
				#self sell
				link = settings.baseUrl
			offers.append(link)
		return offers

	def getPageNumsAndParseFirstPage(self):
		"""From first page, get the total page number; 
		meanwhile parse this page."""
		bsObj = self.createBSObj()

		#get offers from first page
		self.offerlist = self.offerlist + self.pageProcess(bsObj)
		
		#get number of offer list
		ul_pagination = bsObj.select('ul.a-pagination')
		if (len(ul_pagination) == 0):
			return 1
		else:
			lis = ul_pagination[0].select('li')
			return int(lis[-2].text)
	
	def getOffersByPage(self, page):
		"""Get offers from a specific page."""
		bsObj = self.createBSObj(page)
		return self.pageProcess(bsObj)

	def getOffers(self):
		"""Get offers of a item."""
		pageNums = self.getPageNumsAndParseFirstPage()
		for i in range(1, pageNums):
			self.offerlist = self.offerlist + self.getOffersByPage(i+1)
