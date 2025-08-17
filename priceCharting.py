import scrapy


class PriceChartingSpider(scrapy.Spider):
    name = "priceCharting"
    allowed_domains = ["www.pricecharting.com"]
    start_urls = ["https://www.pricecharting.com/console/pokemon-prismatic-evolutions"]

    def parse(self, response):
        """Parse card rows from the PriceCharting table.

        The previous implementation extracted the first card name and price
        from the entire page for every ``td`` element, resulting in the same
        data being yielded repeatedly.  By iterating over each table row and
        using relative XPaths we ensure that each card's information is
        captured correctly.
        """
        # Each card is represented by a table row with a ``title`` cell.
        for card in response.xpath('//tr[td[@class="title"]]'):
            name = card.xpath('./td[@class="title"]/a/text()').get()
            price_text = card.xpath('.//span[@class="js-price"]/text()').get()
            # Guard against missing prices before attempting string replacement
            price = (
                price_text.replace("$", "").replace(",", "")
                if price_text
                else None
            )

            yield {
                "name": name,
                "price": price,
            }
