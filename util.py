# -*- coding: utf-8 -*-

#util functions for scrapying html pages

import urllib2

def getCharset(content):
	"""Get charset of content(html)."""
	return content.headers['content-type'].split('charset=')[-1]

def getDecodedHtml(url):
	"""Get html content from url, decoded with given charset."""
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	#fake browser action
	req = urllib2.Request(url=url, headers=headers)
	html = urllib2.urlopen(req)
	charset = getCharset(html)
	data = html.read()
	html.close()
	return data.decode(charset)
