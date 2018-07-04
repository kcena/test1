#coding:utf-8
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from UrlManager import UrlManager
class SpiderMan(object):
	def __init__(self):
		self.mangaer = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()
	def crawl(self,root_url):
		self.mangaer.add_new_url(root_url)
		while (self.mangaer.has_new_url() and self.mangaer.old_url_size()<100):
			try:
				new_url = self.mangaer.get_new_url()
				html = self.downloader.download(new_url)
				new_urls,data = self.parser.parser(new_url,html)
				self.mangaer.add_new_urls(new_urls)
				self.output.store_data(data)
				print "已经抓取了%s个链接"%self.mangaer.old_url_size()
			except Exception,e:
				print "crawl failed"
		self.output.output_html()
if __name__ == "__main__":
	Spider_man = SpiderMan()
	Spider_man.crawl("http://baike.baidu.com")


			