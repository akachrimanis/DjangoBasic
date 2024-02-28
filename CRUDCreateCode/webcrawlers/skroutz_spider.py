
    
import scrapy
from scrapy.crawler import CrawlerProcess

class SkroutzSpider(scrapy.Spider):
    name = 'skroutz'
    allowed_domains = ['www.skroutz.gr']
    start_urls = ['https://www.skroutz.gr/']

    def parse(self, response):
        # Extract product names
        product_names = response.css('.js-product-title::text').getall()

        # Yield each product name
        for product_name in product_names:
            yield {
                'product_name': product_name.strip()
            }

    def process_item(self, item, spider):
        # Append each product name to the products list
        products.append(item['product_name'])
        return item

# Create a list to store product names
products = []

# Run the spider and store the product names in the list
process = CrawlerProcess(settings={})
process.crawl(SkroutzSpider)
process.start()

# Print the list of product names
print("List of Products:")
for product in products:
    print(product)
