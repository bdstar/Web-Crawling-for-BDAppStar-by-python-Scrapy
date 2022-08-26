import scrapy

class AllSpider(scrapy.Spider):
    name = 'all'
    start_urls = ['https://www.gsmarena.com.bd/brands/']

    def parse(self, response):
        for products in response.css('div.product-thumb'):
            link = products.css('div.product-thumb div.image a').attrib['href']
            image = products.css('div.product-thumb div.image a img').attrib['src']
            name = products.css('div.product-thumb div.text-center b a::text').get()

            yield {
                'link': link,
                'image': image,
                'name': name
            }

        """
        <div class="col-md-3 col-sm-6  col-xs-6">
            <div class="product-thumb">

                <div class="image">
                    <a href="https://www.gsmarena.com.bd/alcatel/">
                        <img class="img-responsive" src="https://www.gsmarena.com.bd/images/brands/Alcatel1486327723.jpg" alt="Alcatel">
                    </a>
                </div>

                <div class="text-center">
                    <b>
                        <a href="https://www.gsmarena.com.bd/alcatel/">Alcatel</a>
                    </b>
                </div>
                
            </div>
        </div>
        """
