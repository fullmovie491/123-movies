import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ExampleSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['123movies.unblockall.org'] # Which (sub-)domains shall be scraped?
    start_urls = ['http://123movies.unblockall.org/movies-genres/action.html'] # Start with this one
    rules = [Rule(LinkExtractor(allow=(r'watch'),deny=(r'season')), callback='watch_page')]#,follow=True)] # Follow any link scrapy finds (that is allowed).

    def watch_page(self,response):

       # print('%s' % response.css('title::text').extract_first())

        for server in response.css('.server_play a::attr(href)'):
        	yield response.follow(server,self.get_server_links)

    def get_server_links(self,response):



    	yield{
    			'url'  : response.url,
    			'title': response.css('title::text').extract_first(),
    			'movie' : response.css('h3::text').extract_first(),
    			'server name' : response.css('.server_playing .server_servername').extract_first(),
    			'embed_code' : response.css('div#media-player  script::text').extract_first(),
    			'direct_link' : response.css('div#media-player  a::attr(href)').extract_first()
    	}
    	

        