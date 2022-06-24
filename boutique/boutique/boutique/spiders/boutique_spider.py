from cgitb import text
from fileinput import filename
import scrapy
 
class BoutiqueSuperPagesSpider(scrapy.Spider):
    name = "superpages"
    
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
      
       for boutique in response.css("div[class='right-card']"):
        yield {
            "nombre": boutique.css("h2::text").extract_first(),
            "teléfono": boutique.css("h3::text").extract_first(),
            "dirección": boutique.css("h4::text").extract_first()
        }


class BoutiqueInfoPaginaSpider(scrapy.Spider):
    name = "infopaginas"
    def start_requests(self):
        urls = [
            "https://infopaginas.com/businesses?q=Boutiques&geo=PR&order=&category=6551&neighborhood=&lat=&lng=&geoLoc=&_route=domain_search_index&_firewall_context=security.firewall.map.context.main&page=1",
            
            "https://infopaginas.com/businesses?q=Boutiques&geo=PR&order=relevance&category=6551&neighborhood=&lat=&lng=&geoLoc=&_route=domain_search_index&_firewall_context=security.firewall.map.context.main&page=2"
        ]
        for i, url in enumerate(urls):
           yield scrapy.Request(
                url=url, callback=self.parse, dont_filter=True, meta={"cookiejar": i}
            )

    def parse(self, response):
        for boutique in response.css('div[data-bw-gtm-component="search-results-item"]'):
            yield { "boutique_info" : boutique.css('a::attr(href)').getall() } 
            
