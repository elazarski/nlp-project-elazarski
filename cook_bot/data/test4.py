# coding: utf-8
from urllib import request
from bs4 import BeautifulSoup as bs
from string import punctuation
url = 'https://www.allrecipes.com/recipes/?page=1000000'
html = request.urlopen(url)
url
# well that works, then
