#!/usr/bin/python

import pandas as pd
import lxml.html as lh
import requests


url='http://pokemondb.net/pokedex/all'
url1='https://en.wikipedia.org/wiki/Main_Page'

# tables = pd.read_html(url)

page = requests.get(url)
doc = lh.fromstring(page.content)
print type(doc)
tr_elements = doc.xpath('//tr')

for t in tr_elements:
    for j in t.iterchildren():
        print j.text_content()
