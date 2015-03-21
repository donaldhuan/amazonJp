import sys
from os import path

sys.path.append(path.dirname(path.abspath(__file__)))

#base settings
baseUrl = 'http://www.amazon.co.jp'
searchPostfix = '/s/?field-keywords='
offerPostfix = '/gp/offer-listing/'
conditions = ['new', 'used', 'refurbished']
offerConditionPostfix = ['?condition='+cond for cond in conditions]
