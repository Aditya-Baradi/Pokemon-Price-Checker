#scrapes website
import scrapy


class PriceChartingSpider(scrapy.Spider):
    name = "priceCharting"
    allowed_domains = ["www.pricecharting.com"]
    start_urls = ["https://www.pricecharting.com/console/pokemon-prismatic-evolutions"]
    
    def parse(self, response):
        for card in response.xpath('//td'):
            yield{
                'name': response.xpath('//td[@class="title"]/a/text()').get(),
                'price': response.xpath('//span[@class="js-price"]//text()').get().replace('$','').replace(',','')
            }
