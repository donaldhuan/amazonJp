import util
from bs4 import BeautifulSoup as bs

class BestSeller:
	"""Get first 3 best sellers of each category(all level)."""

	def __init__(self):
		self.baseUrl = "http://www.amazon.co.jp/gp/bestsellers/"


	def getCategory(self):
		"""get all categories"""
		bsObj = bs(util.getDecodedHtml(self.baseUrl), "lxml")
		lis = bsObj.select("#zg_browseRoot > ul > li > a")
		root_names = ['1-'+li.text for li in lis]
		root_urls = [li.attrs["href"] for li in lis]
		cate_names = []
		cate_urls = []
		for index in range(len(root_urls)):
			cate_names.append(root_names[index])
			cate_urls.append(root_urls[index])
			print root_urls[index]
			child_names, child_urls = self.getLowerCategory(root_urls[index])
			cate_names.extend(child_names)
			cate_urls.extend(child_urls)
		return cate_names, cate_urls

	def getLevel(self):
		return

	def getLowerCategory(self, url):
		"""get lower level categories"""
		cate_names = []
		cate_urls = []
		bsObj = bs(util.getDecodedHtml(url), "lxml")
		li_selected = bsObj.select('#zg_browseRoot .zg_selected')[0].parent

		level = len(li_selected.find_parents("ul"))
		print url
		print level-1
		
		ul_children = li_selected.find_next_siblings("ul")
		if len(ul_children) == 0:
			return [], []

		lis = ul_children[0].select("li > a")
		names = [str(level)+'-'+li.text for li in lis]
		urls = [li.attrs["href"] for li in lis]
		print urls
		for index in range(len(urls)):
			print index
			cate_names.append(names[index])
			cate_urls.append(urls[index])
			child_names, child_urls = self.getLowerCategory(urls[index])
			print child_names
			cate_names.extend(child_names)
			cate_urls.extend(child_urls)
		return cate_names, cate_urls

if __name__ == "__main__":
	seller = BestSeller()
	res1, res2 = seller.getCategory()
	f = open('category.txt', 'w')
	for i in range(len(res1)):
		f.write(res1[i]+'\n')
		f.write(res2[i]+'\n')
	f.close()
