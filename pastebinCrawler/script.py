import httplib as hl
import random
import string

class PastebinCrawler:
	url = "pastebin.com";

	def __init__(self):
		""" Init connection """
		self.httpConnection = hl.HTTPConnection(self.url);
		print "Init connection with pastebin.com ... " + "\033[92mOk\033[0m";
		
	def crawl(self):
			""" Generate page id then request page"""
			generatedNumber = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8));
			requestedPage = "/raw/" + generatedNumber;
			self.httpConnection.request("GET", requestedPage);
			
			""" Get status and response """
			response = self.httpConnection.getresponse();
			if response.status == 200:
				print self.url + requestedPage + " \033[92mFound\033[0m";
				with open(generatedNumber, 'w') as f:
					f.write(response.read());
			else:
				print self.url + requestedPage + " \033[31mNot found\033[0m";
				response.read();	

crawl = PastebinCrawler();
crawl.crawl();
