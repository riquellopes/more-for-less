import os
import pytest
from scrapy.http import HtmlResponse
from app.spiders.smiles import Smiles
from app.item import Item

def read(name = "index"):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, f'./{name}.html')
    return open(file_path, 'rb').read()

@pytest.fixture()
def home(): 
    return HtmlResponse(
        url='https://www.shoppingsmiles.com.br/smiles/index.jsf?a=true', body=read())

def test_should_get_item_jbl_box(home):
    smiles = Smiles(limit=1)
    result = next(smiles.parse(home))
    
    assert Item(
        title="Caixa de Som JBL Charge 5 Bluetooth Portátil - 40W com Tweeter",
        miles='3.330', 
        price='1.109,90', 
        url='/smiles/produto.jsf?f=8&p=2285673_8&n=Caixa+de+Som+JBL+Charge+5+Bluetooth+Port%C3%A1til+-+40W+com+Tweeter&a=true') == result