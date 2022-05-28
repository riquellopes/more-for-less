import scrapy

class Smiles(scrapy.Spider):
    name = 'smiles'
    allowed_domains = ['shoppingsmiles.com.br']

    def parse(self, response, **kwargs):
        return super().parse(response, **kwargs)