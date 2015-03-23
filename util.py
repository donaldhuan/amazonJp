# -*- coding: utf-8 -*-

def getCharset(content):
	"""Get charset of content(html)."""
	return content.headers['content-type'].split('charset=')[-1]
