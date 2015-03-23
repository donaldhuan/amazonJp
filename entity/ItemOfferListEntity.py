# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup as bs
import os
#------
import settings
import util
from retry import retry

class ItemOfferListEntity:
	def __init__(self, asin):
		self.url = settings.baseUrl + settings.offerPostfix + asin + '/'
		self.offerlist = []

	@retry(urllib2.URLError, tries=100, delay=0.1, backoff=1)
	def createBSObj(self, page=1):
		url = self.url+'?startIndex='+str(10*(page-1))
		bsObj = bs(util.getDecodedHtml(url), 'lxml')
		return bsObj

	def pageProcess(self, bsObj):
		div_olpOffer = bsObj.select('div.olpOffer')
		offers = []
		for offer in div_olpOffer:
			div_seller = offer.select('div.olpSellerColumn')[0]
			try:
				link = div_seller.select('a')[0].attrs['href']
			except:
				#self sell
				link = settings.baseUrl
			offers.append(link)
		return offers

	def getPageNumsAndParseFirstPage(self):
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
		bsObj = self.createBSObj(page)
		return self.pageProcess(bsObj)

	def getOffers(self):
		pageNums = self.getPageNumsAndParseFirstPage()
		for i in range(1, pageNums):
			self.offerlist = self.offerlist + self.getOffersByPage(i+1)
