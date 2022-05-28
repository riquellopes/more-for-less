import os
import pytest
from scrapy.http import HtmlResponse
from app.spiders.smiles import Smiles

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