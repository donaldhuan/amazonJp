import util
from bs4 import BeautifulSoup as bs
import csv

class BestSeller:
	"""Get first 3 best sellers of each category(all level)."""

	def __init__(self):
		self.baseUrl = "http://www.amazon.co.jp/gp/bestsellers/"
		with open('bestseller.csv', 'a') as csvfile:
			fieldnames = ['category_name', 'category_url', 'item1_name', 
					'item1_url', 'item2_name', 'item2_url', 'item3_name', 
					'item3_url']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()


	def getCategory(self):
		"""get all categories"""
		bsObj = bs(util.getDecodedHtml(self.baseUrl), "lxml")
		lis = bsObj.select("#zg_browseRoot > ul > li > a")
		root_names = ['1-'+li.text.strip() for li in lis]
		root_urls = [li.attrs["href"].strip() for li in lis]
		for index in range(len(root_urls)):
			#print '------------------------------------------------------------'
			self.getLowerCategory(root_urls[index], root_names[index])

	def getLowerCategory(self, url, name):
		"""get lower level categories"""
		bsObj = bs(util.getDecodedHtml(url), "lxml")

		#parse best 3 seller
		try:
			links = bsObj.select('.zg_itemRow .zg_title a')
			item1_name = links[0].text.strip()
			item1_url = links[0].attrs['href'].strip()
			item2_name = links[1].text.strip()
			item2_url = links[1].attrs['href'].strip()
			item3_name = links[2].text.strip()
			item3_url = links[2].attrs['href'].strip()
		except:
			item1_name = ''
			item1_url = ''
			item2_name = ''
			item2_url = ''
			item3_name = ''
			item3_url = ''

		#record to csv file
		with open('bestseller.csv', 'a') as csvfile:
			fieldnames = ['category_name', 'category_url', 'item1_name', 
					'item1_url', 'item2_name', 'item2_url', 'item3_name', 
					'item3_url']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writerow({'category_name': name.encode('utf-8'), 
				'category_url': url, 
				'item1_name': item1_name.encode('utf-8'), 
				'item1_url': item1_url, 
				'item2_name': item2_name.encode('utf-8'), 
				'item2_url': item2_url, 
				'item3_name': item3_name.encode('utf-8'), 
				'item3_url': item3_url
			})

		#print url
		try:
			li_selected = bsObj.select('#zg_browseRoot .zg_selected')[0].parent

			level = len(li_selected.find_parents("ul"))
			#print level-1
		except:
			f = open('exception.txt', 'a')
			f.write(url+'\n')
			f.close()
			return
		
		ul_children = li_selected.find_next_siblings("ul")
		if len(ul_children) == 0:
			return
		
		#parse child category
		lis = ul_children[0].select("li > a")
		names = [str(level)+'-'+li.text.strip() for li in lis]
		urls = [li.attrs["href"].strip() for li in lis]

		for index in range(len(urls)):
			self.getLowerCategory(urls[index], names[index])

if __name__ == "__main__":
	seller = BestSeller()
	seller.getCategory()
