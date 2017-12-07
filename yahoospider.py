import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoospider'
    start_urls = ['https://news.yahoo.co.jp/']

    def parse(self, response):
        print("start")
        for title in response.css(".topics .ttl a::text"):
            print(title.extract())
