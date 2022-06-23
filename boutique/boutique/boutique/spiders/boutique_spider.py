from cgitb import text
from fileinput import filename
import scrapy
 
class BoutiqueSpider(scrapy.Spider):
    name = "boutique"
    
    def start_requests(self):
        urls = [
            "https://www.superpagespr.com/'Boutiques'?showQuantity=100&currentPage=1",
            
            "https://www.superpagespr.com/'Boutiques'?showQuantity=100&currentPage=2"
        ]
        for i, url in enumerate(urls):
           yield scrapy.Request(
                url=url, callback=self.parse, dont_filter=True, meta={"cookiejar": i}
            )
            
    
    def parse(self, response):
       page = response.url.split("/")[-2]
       filename = f'boutiques-{page}.html'
       with open(filename, 'wb') as f:
            f.write(response.body)
       self.log(f'Saved file {filename}')

       for boutique in response.css("div[class='right-card']"):
        yield {
            "nombre": boutique.css("h2::text").extract_first(),
            "teléfono": boutique.css("h3::text").extract_first(),
            "dirección": boutique.css("h4::text").extract_first()
        }
