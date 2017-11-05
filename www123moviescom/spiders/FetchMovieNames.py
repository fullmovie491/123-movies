import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

id = 0

class FetchMovieNamesSpider(CrawlSpider):
    name = 'FetchMovieNames'
    allowed_domains = ['123movies.unblockall.org'] # Which (sub-)domains shall be scraped?
    start_urls = ['http://123movies.unblockall.org'] # Start with this one
    rules = [Rule(LinkExtractor(allow=(r'\/watch\/'),deny=(r'(season|\/watch\/.+\/|episode)')), callback='get_movie_details',follow=True)] # Follow any link scrapy finds (that is allowed).
    

    def get_movie_details(self,response):
    	
    	if not (re.search(r'(season|episode)',response.css('title::text').extract_first(),re.IGNORECASE)):
    		#if not (response.css('#details.section-box')):
		    	global id
		    	if (response.css('#details.section-box')):
		    		v_type = 'Sea'
		    	else:
		    		v_type = 'Mov'
		    	year = response.css('.mvici-right p:nth-child(4)::text').extract_first()
		    	year = year.replace('(','')
		    	year = year.replace(')','')
		    	movie = response.css('h3::text').extract_first()
		    	movie = movie.replace('~','-')
		    	print('%i' % id +'~%s' % movie + '~%s' % v_type +'~%s' % year + '~%s' % response.url)
		        id = id + 1
		        #meed to see if its a episode related by comparing element details,section-box
		        #need to replace ~ in title field  to something else
		    	# yield{
		    	# 		'url'  : response.url,
		    	# 		'title': response.css('title::text').extract_first(),
		    	# 		'movie' : response.css('h3::text').extract_first(),
		    	# 		'desc' : response.css('#mv-info .desc::text').extract_first(), # need to chekc to get only part of descrip
		    	# 		'actor' : response.css('.mvici-left p:nth-child(2) a::text').extract_first(),
		    	# 		'director' : response.css('.mvici-left p:nth-child(3) a::text').extract_first(),
		    	# 		'year' : response.css('.mvici-right p:nth-child(4)::text').extract_first()

		    	# }
    	

        