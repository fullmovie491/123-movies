import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class FetchServerLinksSpider(CrawlSpider):
    name = 'FetchServerLinks'
    global embed_list
    embed_list = []
    allowed_domains = ['http://123moviesonline.stream']#123movies.unblockall.org'] # Which (sub-)domains shall be scraped?
    start_urls = ['http://123moviesonline.stream/watch/QG3oA8Go-hack-sign-sub.html'] # Start with this one
    rules = [Rule(LinkExtractor(allow=(r'\/watch\/'),deny=(r'(season|\/watch\/.+\/|episode)')), callback='watch_page',follow=True)]# Follow any link scrapy finds (that is allowed).

    def watch_page(self,response):
        main_url = response.url
    	if not (re.search(r'(season|episode)',response.css('title::text').extract_first(),re.IGNORECASE)):
    		if not (response.css('#details.section-box')):
		        for server in response.css('.server_play a::attr(href)').extract():
		            yield response.follow(server,self.get_server_links,meta={'main_url':main_url})
                print embed_list
            
               

    def get_server_links(self,response):

        embed_list.append(response.css('div#media-player  script::text').extract_first())
        
    	yield{
                'main_url' : response.meta.get('main_url'),
    			'url'  : response.url,
    			'title': response.css('title::text').extract_first(),
    			'movie' : response.css('h3::text').extract_first(),
    			'server name' : response.css('.server_playing .server_servername::text').extract_first(),
    			'embed_code' : response.css('div#media-player  script::text').extract_first(),
    			'direct_link' : response.css('div#media-player  a::attr(href)').extract_first()
    	}
    	

        