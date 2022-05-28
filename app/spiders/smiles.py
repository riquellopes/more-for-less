import scrapy
from app.item import Item

class Smiles(scrapy.Spider):
    name = 'smiles'
    allowed_domains = ['shoppingsmiles.com.br']

    def parse(self, response):
        boxes = response.css("span.slider-item.box-produto")

        for box in boxes:
            miles = box.css("span.num-ganhe::text").extract_first()
            price = box.css("span.preco-por.preco-por-acumulo:last-child::text").extract_first()
            url = box.css("a::attr(href)").extract_first()
            yield Item(url=url, price=price, miles=miles)