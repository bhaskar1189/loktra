import bs4
import urllib2
import argparse

class ShoppingSpider:

	def __init__(self):
		pass

	def get_number(self, text):
		regex = re.compile(r'\d+')
		num = regex.findall(text)
		num = [int(i) for i in num]
		return max(num)

	def crawler(self, keyword , pagenumber = None):
		if pagenumber == None :
			url = 'http://www.shopping.com/products?KW=%s'%(keyword)
			html = urllib2.urlopen(url)
			soup = bs4.BeautifulSoup(html, 'html.parser')
			try:
				spans = soup.find_all('span', attrs={'class':'numTotalResults'})
				return self.get_number(spans[0].getText())
			except:
				return "No matches for %s"%(keyword)
		else:
			url = 'http://www.shopping.com/products~PG-%s?KW=%s'%(pagenumber,keyword)
			html = urllib2.urlopen(url)
			soup = bs4.BeautifulSoup(html, 'html.parser')
			try:
				spans = soup.find_all('span', attrs={'class':'quickLookGridItemFullName hide'})
				for i in spans:
					print i.getText()
			except:
				return "No matches for %s"%(keyword)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Scrape shopping.com')
	parser.add_argument('key_word', help='Search keyword')
	parser.add_argument('page_number', default=None, nargs='?',help='Search results page number')
	args = parser.parse_args()

	try:
		crawler = ShoppingSpider()

		if args.page_number:
			crawler.crawler(args.key_word, args.page_number)
		else:
			print "Total of",crawler.crawler(args.key_word),"results"
	except ValueError:
		parser.print_help()