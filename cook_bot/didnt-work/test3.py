# coding: utf-8
from urllib import request
from bs4 import BeautifulSoup as bs
url = 'https://www.allrecipes.com/recipe/25203/brown-sugar-meatloaf/?internalSource=hub%20recipe&amp;referringContentType=Recipe%20Hub'
html = request.urlopen(url)
soup = bs(html, 'html.parser')
soup
soup.findAll(name='span', attrs='recipe-ingred_txt added')
spans = soup.findAll(name='span', attrs='recipe-ingred_txt added')
while ingred = spans.pop():
spans.index
spans.count
spans.count()
len(spans)
for i in range(len(spans)):
    span = spans.pop()
    print(span.contents[0])
    
spans = soup.findAll(name='span', attrs='recipe-ingred_txt added')
ingredients = []
import re
from string import punctuation
for i in range(len(spans)):
    span = spans.pop()
    ingredients.append(span.contents)
    
ingredients
ingredients[0]
ingredients = []
for i in range(len(spans)):
    span = spans.pop()
    ingredients.append(span.contents[0])
    
ingredients
spans = soup.findAll(name='span', attrs='recipe-ingred_txt added')
for i in range(len(spans)):
    span = spans.pop()
    ingredients.append(span.contents[0])
    
ingredients
i = ingredients[0]
re.search(i, '\D')
i
re.search('\D', i)
re.find('\D', i)
re.split('\D', i)
i
re.findall('\D', i)
re.findall('\D', i).join()
''.join(re.findall('\D', i))
re.sub('\D', i)
re.sub('\D',' ', i)
re.sub(r'\d',' ', i)
remove_chars = '1234567890'
punctuation
remove_chars += punctuation
remove_chars
'a' in remove_chars
'1' in remove_chars
ingred
ingredients
spans = soup.findAll(name='span', attrs='recipe-ingred_txt added')
ingredients = []
for i in range(len(spans)):
    span = spans.pop()
    ingrd = span.contents[0]
    
    
t = 'abc123'
t.replace(remove_chars, '')
t.split()
t.split('')
[c for c in t]
for i in range(len(spans)):
    span = spans.pop()
    ingrd = span.contents[0]
    chars = [c for c in ingrd if c not in remove_chars]
    
chars
a [c for c in t]
a = [c for c in t]
''.join(a)
for i in range(len(spans)):
    span = spans.pop()
    ingrd = span.contents[0]
    chars = [c for c in ingrd if c not in remove_chars]
    ingredients.append(''.join(chars))
    
ingredients
spans = soup.findAll(name='span', attrs='recipe-ingred_txt added')
for i in range(len(spans)):
    span = spans.pop()
    ingrd = span.contents[0]
    chars = [c for c in ingrd if c not in remove_chars]
    ingredients.append(''.join(chars))
    
ingredients
ingredients[0].trim()
i = ingredients[0]
i.strip()
spans = soup.findAll(name='span', attrs='recipe-ingred_txt added')
ingredients = []
for i in range(len(spans)):
    span = spans.pop()
    ingrd = span.contents[0]
    chars = [c for c in ingrd if c not in remove_chars]
    ingredients.append(''.join(chars).strip())
    
    
ingredients
