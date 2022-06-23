# Scraper for boutiques in Puerto Rico
## Using a scrapy spider, I have retrieved the data about boutiques in PR, which added up to 180 with directions, phone numbers and addresses

###To use, please install a virtual environment with venv per the scrapy documentation. [Scrapy documentation](https://docs.scrapy.org/en/latest/ "Scrapy Documentation") And then on the top folder of the scraper run:

<pre><code>scrapy crawl -o boutique boutique.csv</code></pre>

This will crawl both sites on the list and retrieve the boutique's information. 


## Using the scrapy shell to get css elements. 

To get the css elements run a scrapy shell and follow the instructions on the documentation. For superpagespr.com, the elements were easily obtained with the h2, h3 and h4 tags. 