import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_crawler.items import Article

class WikipediaspiderSpider(CrawlSpider):
    
    name = 'WikipediaSpider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/sleep']

    #this rule means that every wiki link that we come across we will crawl into it
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_article', follow=True)]

    def parse_article(self, response):
        article = Article() #article is an item object and it acts like a dict
        
        article['title']= response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()')
        article['url'] = response.url

        article['last_updated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
