# coding: utf-8
from urllib import request
from bs4 import BeautifulSoup as bs
base_url = 'https://www.allrecipes.com/recipes/?page='
i = 1
page_url = base_url + i
page_url = base_url + str(i)
page_url
html = request.urlopen(page_url)
soup = bs(html, 'html.parser')
soup.findAll(name='div', attrs='fixed-recipe-card')
soup.findAll(name='article', attrs='fixed-recipe-card')
recipes = []
recipe_names = []
soup.findAll(name='article', attrs='fixed-recipe-card').pop()
r = soup.findAll(name='article', attrs='fixed-recipe-card').pop()
r
r
r.findAll(name='span', attrs='fixed-recipe-card__title-link')
r.findAll(name='span', attrs='fixed-recipe-card__title-link')[0]
r.findAll(name='span', attrs='fixed-recipe-card__title-link').pop()
r.findAll(name='span', attrs='fixed-recipe-card__title-link').pop().contents()
r.findAll(name='span', attrs='fixed-recipe-card__title-link').pop().contents
r.findAll(name='span', attrs='fixed-recipe-card__title-link').pop().contents[0]
name = r.findAll(name='span', attrs='fixed-recipe-card__title-link').pop().contents[0]
if name not in recipe_names:
    recipe_names.append(name)
    
recipe_names
if name not in recipe_names:
    recipe_names.append(name)
    
recipe_names
r.findAll(name='div', attrs='fixed-recipe-card__info')
info = r.findAll(name='div', attrs='fixed-recipe-card__info')
info = r.findAll(name='div', attrs='fixed-recipe-card__info').pop
info
info = r.findAll(name='div', attrs='fixed-recipe-card__info').pop()
info
name = info.findAll(name='span', attrs='fixed-recipe-card__title-link').pop().contents[0]
name
title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link')
title_link
attrs = title_link.attrs
title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link').pop()
attrs = title_link.attrs
attrs['href']
recipe_url = attrs['href']
recipe_html = request.urlopen(recipe_url)
recipe_soup = bs(recipe_html, 'html.parser')
recipe_soup.findAll(name='span', attrs='recipe_ingred_txt added')
recipe_soup.findAll(name='span', attrs='recipe-ingred_txt added')
ingredients = []
ingred_spans = recipe_soup.findAll(name='span', attrs='recipe-ingred_txt added')
from string import punctuation
remove_chars = '1234567890' + punctuation
remove_chars
for i in range(len(ingred_spans)):
    ing = ingred_spans.pop()
    ing = ing.replace(remove_chars, '')
    ingredients.append(ing.strip())
    
ingred_spans
ingred_spans = recipe_soup.findAll(name='span', attrs='recipe-ingred_txt added')
for i in range(len(ingred_spans)):
    ing = ingred_spans.pop()
    ing = ing.contents[0]
    ing = ing.replace(remove_chars, '')
    ingredients.append(ing.strip())
    
ingredients
ingredients = []
ingred_spans = []
ingred_spans = recipe_soup.findAll(name='span', attrs='recipe-ingred_txt added')
for i in range(len(ingred_spans)):
    span = ingred_spans.pop()
    ingrd = span.contents[0]
    chars = [c for c in ingrd if c not in remove_chars]
    ingrd = ''.join(chars)
    ingredients.append(ingrd.strip())
    
ingredients
ol = recipe_soup.findAll(name='ol', attrs='breadcrumbs breadcrumbs').pop()
ol
spans = ol.findAll(name='span', attrs='toggle-similar__title')
spans
category = spans.pop()
category
category = spans.pop().contents[0]
category
category = spans.pop().contents[0].strip()
category
