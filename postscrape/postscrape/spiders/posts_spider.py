import scrapy

class PhoneSpider(scrapy.Spider):
    name = 'phone'
    start_urls = ['https://www.gsmarena.com.bd/vivo-s10e/']

    def parse(self, response):
        data = {}
        for products in response.css('tr'):
            label = products.css('td.specs_name::text').get()
            value = products.css('td.specs_name2::text').get()

            if label is None:
                label = products.css('td div.specs_name::text').get()

            if (value is None) or (value is "\n"):
                value = products.css('td.specs_name2 a::text').get()   
            
            if (label is not None) and (value is not None):
                data[label] = value

        yield {
            "phone" : "smartphone",
            "data" : data
        }

        """
        <div class="col-xs-12 col-sm-6">
            <a href="https://www.gsmarena.com.bd/pictures/apple-iphone-14-pro-max/">
            <img src="https://www.gsmarena.com.bd/images/products/Apple-iPhone-14Pro-Max.jpg" width="400" alt="Apple iPhone 14 Pro Max" title="Apple iPhone 14 Pro Max"></a>
        </div>


        <tr>
            <td class="specs_name">Name</td>
            <td class="specs_name2">Apple iPhone 14 Pro Max</td>
        </tr>
        <td class="specs_name2"><a href="https://www.gsmarena.com.bd/apple/">Apple</a></td>
        <td class="specs_name2"><a href="https://www.gsmarena.com.bd/apple-iphone-14-pro-max/">Super Retina XDR OLED, 120Hz, HDR10, Dolby Vision, 1000 nits (HBM), 1200 nits (peak)</a>

        for products in response.css('div.product-item-info'):
            try:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': products.css('span.price::text').get().replace('£',''),
                    'link': products.css('a.product-item-link').attrib['href'],
                }
            except:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'link': products.css('a.product-item-link').attrib['href'],
                }
        
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        """
