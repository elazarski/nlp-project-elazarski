# coding: utf-8
from urllib import request
import BeautifulSoup
from BeautifulSoup import BeautifulSoup as BS
from bs4 import BeautifulSoup as bs
url = 'https://www.allrecipes.com/recipes/?page=1'
html = request.urlopen(url)
soup = bs(html)
soup.findAll(name='article')
soup.findAll(name='article')[0]
soup.findAll(name='article' attrs='fixed-recipe-card')
soup.findAll(name='article' attrs=['fixed-recipe-card'])
soup.findAll(name='article', attrs='fixed-recipe-card')
recipe_cards = soup.findAll(name='article', attrs='fixed-recipe-card')
recipe_cards[0]
r=recipe_cards
r.source
r.source()
r.index
r.index()
r.index(1)
r.index('a')
r.source()
r.source
r
soup
soup.prettify()
p = soup.prettify()
r
get_ipython().magic('clear ')
print("==============================================================================================================================================================================")
r
recipe_cards
recipe_cards.pop
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards.pop()
recipe_cards = soup.findAll(name='article', attrs='fixed-recipe-card')
r = recipe_cards.pop()
r
r.find_all(name='span', attrs='fixed-recipe-card__title-link')
title_span = r.find_all(name='span', attrs='fixed-recipe-card__title-link')
title_span.pop()
title = title_span.pop()
title_span = r.find_all(name='span', attrs='fixed-recipe-card__title-link')
title = title_span.pop()
title
title.contents
info = r.findAll(name='div', attrs='fixed-recipe-card__info')
info
i = info.pop()
i
i.find(name='a', attrs='hub recipe')
i.find(name='a', attrs='fixed-recipe-card__title-link ng-isolate-scope')
i.find(name='a', attrs='hub recipe', recursive=True)
i.find(name='a', attrs='fixed-recipe-card__title-link ng-isolate-scope', recursive=True)
i.findAll(name='a', attrs='hub recipe')
i.findAll(name='a', attrs='hub recipe', recursive=True)
i.findAll(name='a', attrs='fixed-recipe-card__title-link ng-isolate-scope', recursive=True)
i.findAll(name='a')
i.findAll(name='a', attrs='fixed-recipe-card__title-link')
l = i.findAll(name='a', attrs='fixed-recipe-card__title-link')
l
l = l.pop()
l
l.contents
l.decode_contents()
l.attrs
attrs = l.attrs
attrs['href']
for r in recipe_cards:
    info = r.findAll(name='div', attrs='fixed-recipe-card__info').pop()
    title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link').pop()
    attrs = title_link.attrs
    print(attrs['href'])
    
for r in recipe_cards:
    info = r.findAll(name='div', attrs='fixed-recipe-card__info').pop()
    title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link').pop()
    attrs = title_link.attrs
    print(attrs['href'])
    
l.contents
span = l.contents
span
l.children
l.children()
l.descendants
l.find(name='span')
span = l.find(name='span').pop()
span = l.find(name='span')
span
span.contents
span.contents[0]
for r in recipe_cards:
    info = r.findAll(name='div', attrs='fixed-recipe-card__info').pop()
    title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link').pop()
    attrs = title_link.attrs
    
    print(attrs['href'])
    
titles = []
for r in recipe_cards:
    info = r.findAll(name='div', attrs='fixed-recipe-card__info').pop()
    title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link').pop()
    attrs = title_link.attrs
    span = title_link.find(name='span')
    title = span.contents[0]
    if not title in titles:
        print(attrs['href'])
        titles += title
        
    
titles
titles = []
for r in recipe_cards:
    info = r.findAll(name='div', attrs='fixed-recipe-card__info').pop()
    title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link').pop()
    attrs = title_link.attrs
    span = title_link.find(name='span')
    title = span.contents[0]
    if not title in titles:
        print(attrs['href'])
        titles.append(title)
        
        
    
titles
