import httplib as hl
import random
import string

class PastebinCrawler:
	url = "www.pastebin.com";

	def __init__(self):
		""" Init connection """
		self.httpConnection = hl.HTTPConnection(self.url);
		print "Init connection with pastebin.com ... " + "\033[92mOk\033[0m";
		
	def crawl(self):
		while True:
			""" Generate page id then request page"""
			requestedPage = "/raw/" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8));
			self.httpConnection.request("GET", requestedPage);
			
			""" Get status and response """
			response = self.httpConnection.getresponse();
			if response.status == 400:
				print self.url + requestedPage + " \033[92mFound\033[0m";
				with open(requestedPage, 'w+') as f:
					f.write(response.read());
			else:
				print self.url + requestedPage + " \033[31mNot found\033[0m";
				response.read();	

crawl = PastebinCrawler();
crawl.crawl();
