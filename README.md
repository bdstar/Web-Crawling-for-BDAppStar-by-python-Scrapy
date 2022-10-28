## **Web-Crawling-for-BDAppStar-by-python-Scrapy**

Scrapy is an open-source and collaborative framework for extracting the data you need from websites.

---

## **Check Python**

Open **CMD** to your project folder.

Write “python” to check the python version. Also, write a simple python code to check if it works fine. Now, to exit it, to return to this python environment.

```plaintext
$ python
>> print("hello")
>> exit()
```

Check the python version individually

```plaintext
$ python --version
```

Check the pip version

```plaintext
$ pip -V
```

Upgrade the pip version

```plaintext
$ python -m pip install --upgrade pip
```

If the upgrade PIP fails due to administration permission, then run the following command,

```plaintext
$ python -m  pip install --upgrade pip
```

To check the list of packages with the version currently installed.

```plaintext
$ python -m pip list
```

## Create Virtual Environment

Create a Virtual Environment with this command.

```plaintext
E:\code\python\ecommerce> python -m venv myenv
```

Activate Virtual Environment by **CMD** in Windows OS

```plaintext
E:\code\python\ecommerce> .\myenv\Scripts\activate.bat
```

Activate Virtual Environment by **PowerShell** in Windows OS

```plaintext
E:\code\python\ecommerce> .\myenv\Scripts\Activate.ps1
```

Create a requirements text file

```plaintext
(myenv) E:\code\python\ecommerce> pip freeze > requirments.txt
```

Install python libraries according to the requirements text file

```plaintext
(myenv) E:\code\python\ecommerce> pip install -r requirments.txt
```

Deactivate Virtual Environment by **CMD** in Windows OS

```plaintext
(myenv) E:\code\python\ecommerce> .\myenv\Scripts\deactivate.bat
```

## Install scrapy

```plaintext
(myenv) E:\code\python\ecommerce> pip install scrapy
```

## Create Scrapy Project

```plaintext
(myenv) E:\code\python\ecommerce>scrapy startproject postscrape
```

It will create a project folder directory such as below,

```plaintext
ecommerce/
|- myenv/
|- postscrape/
 |- postscrape/
  |- _pycache_/
  |- spiders/
   |- _pycache_/
   |- _inti_.py
  |- _init.py_
  |- items.py
  |- middlewares.py
  |- pipelines.py
  |- settings.py
 |- scrapy.cfg
|- requirments.txt
```

## Create Scrapy Project

Create a file inside “`spiders`” folder that is “`posts_spider.py`”

```plaintext
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
```

## Run Scrapy Project

```plaintext
You can start your first spider with:
   cd postscrape
   scrapy genspider example example.com
```

```plaintext
(myenv) E:\code\python\ecommerce>cd postscrape
```

```plaintext
(myenv) E:\code\python\ecommerce\postscrape>scrapy crawl phones
```

You can import the output as .json file

```plaintext
(myenv) E:\code\python\ecommerce\postscrape>scrapy crawl phones -o phones.json
```

## References

[Scrapy Website](https://scrapy.org/)

[Intro To Web Crawlers & Scraping With Scrapy](https://www.youtube.com/watch?v=ALizgnSFTwQ)

[The Complete Guide to Python Virtual Environments, activate, deactivate & Requirements.txt](http://techntuts.com/story/The-Complete-Guide-Python-Virtual-Environments-activate-deactivate-Requirements.txt)

[Markdown Editor](https://onlinemarkdowneditor.dev/)