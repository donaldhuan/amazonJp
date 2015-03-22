import urllib2
from bs4 import BeautifulSoup as bs
import os
#------
import settings
from retry import retry

class ItemOfferListEntity:
	def __init__(self, asin):
		
