import requests 
import csv
from retry import retry
from settings import retry_setting

@retry(requests.exceptions.ConnectionError, tries=retry_setting['times'], delay=retry_setting['delay'], backoff=retry_setting['backoff'])
def convert(asin):
	'''give a asin, return the jancode'''
	if asin == '':
		return ''
	url = 'http://erwinmayer.com/emlabs/asin2ean/processing3.php'
	headers = {'X-Requested-With': 'XMLHttpRequest'}
	data = {"locale": "co.jp", "s": "", "searchIndex": "All", "ids": asin, "mode": "ASIN-to-EAN"}
	r = requests.post(url, data=data, headers=headers)
	try:
		return r.json()['result'][asin]
	except:
		return 'No code.'

def getAsin(url):
	'''get asin from the product url'''
	if url == '':
		return ''
	return url.split('/dp/')[1].split('/')[0]

def transfer():
	'''transfer the context in the bestseller.csv'''
	source_file = open('bestseller.csv')
	reader = csv.DictReader(source_file)
	target_file = open('product.csv', 'a')
	fieldnames = list(reader.fieldnames)
	fieldnames.insert(4, 'item1_jancode')
	fieldnames.insert(7, 'item2_jancode')
	fieldnames.insert(10, 'item3_jancode')
	writer = csv.DictWriter(target_file, fieldnames=fieldnames)
	writer.writeheader()
	for row in reader:
		writer.writerow({
			'category_name': row['category_name'], 
			'category_url': row['category_url'], 
			'item1_name': row['item1_name'], 
			'item1_url': row['item1_url'],
			'item1_jancode': convert(getAsin(row['item1_url'])),
			'item2_name': row['item2_name'], 
			'item2_url': row['item2_url'], 
			'item2_jancode': convert(getAsin(row['item2_url'])),
			'item3_name': row['item3_name'], 
			'item3_url': row['item3_url'],
			'item3_jancode': convert(getAsin(row['item3_url']))
		})

if __name__ == "__main__":
	transfer()
