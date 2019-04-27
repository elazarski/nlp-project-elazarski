# coding: utf-8
from urllib import request
from bs4 import BeautifulSoup
url = 'https://www.allrecipes.com/recipe/9023/baked-teriyaki-chicken/?internalSource=previously%20viewed&referringContentType=Homepage&clickId=cardslot%2015'
html = request.urlopen(url)
soup = BeautifulSoup(html)
soup = BeautifulSoup(html, 'html.parser')
soup
html
soup = BeautifulSoup(html)
soup
html
html.code
html.begin
html.read
html.read()
html = request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
soup
soup.findAll(name='ol', attrs='breadcrumbs breadcrumbs')
ol = soup.findAll(name='ol', attrs='breadcrumbs breadcrumbs')
ol.pop()
ol
ol = soup.findAll(name='ol', attrs='breadcrumbs breadcrumbs').pop()
ol
for item in ol.children:
    print(item)
    
for item in ol.children:
    print(item)
    print('--------------')
    
ol
ol.findAll(name='span', attrs='toggle-similar__title')
spans = ol.findAll(name='span', attrs='toggle-similar__title').pop()
spans
spans.contents
spans.contents[0]
spans.contents[0].strip()
