# -*- coding: utf-8 -*-
import scrapy


class A123moviesSpider(scrapy.Spider):
    name = 'a123movies'
    allowed_domains = ['http://123movies.unblockall.org/watch/Ed9b30vY-jeepers-creepers-3.html']
    start_urls = ['http://123movies.unblockall.org/watch/Ed9b30vY-jeepers-creepers-3.html']
    
    def parse(self, response):
        self.log('Just visited:' + response.url)
        yield{
            'iframe':response.css('div#media-player>script::text')[0].extract(),
            }
