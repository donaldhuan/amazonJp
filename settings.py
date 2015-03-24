# -*- coding: utf-8 -*-

import sys
from os import path

sys.path.append(path.dirname(path.abspath(__file__)))

#base settings
baseUrl = 'http://www.amazon.co.jp'

searchPostfix = '/s/?field-keywords='
searchFileds = [
			'aps',
			'digital-text',
			'instant-video',
			'digital-music',
			'mobile-apps',
			'stripbooks',
			'english-books',
			'popular',
			'classical',
			'dvd',
			'videogames',
			'software',
			'computers',
			'electronics',
			'office-products',
			'kitchen',
			'pets',
			'hpc',
			'beauty',
			'food-beverage',
			'baby',
			'apparel',
			'shoes',
			'watch',
			'jewelry',
			'toys',
			'hobby',
			'mi',
			'sporting',
			'automotive',
			'diy',
			'appliances',
			'financial',
			'gift-cards'
		]
searchFieldPostfix = ['&search-alias='+field for field in searchFileds]

offerPostfix = '/gp/offer-listing/'
conditions = ['new', 'used', 'refurbished']
offerConditionPostfix = ['&condition='+cond for cond in conditions]

retry_setting = {'times': 100, 'delay': 0.1, 'backoff': 1}
