import scrapy

class MainSpider(scrapy.Spider):
    name = 'main'
    start_urls = ['https://www.gsmarena.com.bd/brands/']

    def parse(self, response):
        #urls = []
        for brands in response.css('div.product-thumb'):
            #urls.append(brands.css('div.product-thumb div.image a').attrib['href'])
            url = brands.css('div.product-thumb div.image a').attrib['href']
            #bimage = brands.css('div.product-thumb div.image a img').attrib['src']
            #bname = brands.css('div.product-thumb div.text-center b a::text').get()
            #for url in urls:
            #yield scrapy.Request(url=url, callback=self.phones, meta={'bimage': bimage, 'bname': bname})
            yield scrapy.Request(url=url, callback=self.phones)
        #print(urls)
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def phones(self, response):
        for phones in response.css('div.product-thumb'):
            link = phones.css('div.product-thumb a').attrib['href']
            pimage = phones.css('div.product-thumb a img').attrib['src']
            pname = phones.css('div.mobile_name::text').get()

            #yield scrapy.Request(url=link, callback=self.posts, meta={'pimage': pimage, 'pname': pname, 'bimage': response.meta['bimage'], 'bname': response.meta['bname']})
            yield scrapy.Request(url=link, callback=self.posts, meta={'pimage': pimage, 'pname': pname})
        
        next_page = response.css('.pagination > li:last-child > a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.phones)
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def posts(self, response):
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
            "brand" : response.meta['pname'],
            "image" : response.meta['pimage'],
            "data" : data
        }