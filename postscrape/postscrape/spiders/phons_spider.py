import scrapy

class PhonesSpider(scrapy.Spider):
    name = 'phones'
    start_urls = ['https://www.gsmarena.com.bd/xiaomi/']

    def parse(self, response):
        for products in response.css('div.product-thumb'):
            link = products.css('div.product-thumb a').attrib['href']
            image = products.css('div.product-thumb a img').attrib['src']
            name = products.css('div.mobile_name::text').get()

            yield {
                'link': link,
                'image': image,
                'name': name
            }

        next_page = response.css('.pagination > li:last-child > a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        """
        <div class="col-xs-6 col-sm-4 col-md-3">
            <div class="product-thumb">
                <a href="https://www.gsmarena.com.bd/apple-iphone-14-pro/" title="Apple iPhone 14 Pro">
                    <img class="img-responsive" src="https://www.gsmarena.com.bd/images/products/thumb/Apple-iPhone-14Pro.jpg" alt="Apple iPhone 14 Pro" width="200" height="200">
                    <div class="mobile_name">Apple iPhone 14 Pro</div>
                    </a>
                    <div class="mobile_price"></div>
                
                <a href="https://www.gsmarena.com.bd/apple-iphone-14-pro/" title="Apple iPhone 14 Pro">View Details</a>
            </div>
        </div>
        """
