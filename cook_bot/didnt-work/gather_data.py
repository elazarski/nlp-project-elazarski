#!/usr/bin/python3

# imports
from urllib import request
from bs4 import BeautifulSoup as bs
from string import punctuation
import csv

# starting variables
base_url = 'https://www.allrecipes.com/recipes/?page='
page = 1
more_pages = True

recipe_names = []
recipes = []

remove_chars = '1234567890' + punctuation

# read all the pages!
while more_pages:
    print("reading page {0}".format(page))
    page_url = base_url + str(page)
    page_html = None
    page += 1

    # exception when a new page isn't found
    try:
        page_html = request.urlopen(page_url)
    except:
        more_pages = False
        continue

    # parse page so that it can be used
    page_soup = bs(page_html, 'html.parser')

    # loop through recipes on page
    recipe_cards = page_soup.findAll(name='article', attrs='fixed-recipe-card')
    for i in range(len(recipe_cards)):

        # check if recipe has already been done
        recipe_card = recipe_cards.pop()
        info = recipe_card.findAll(name='div', attrs='fixed-recipe-card__info').pop()
        title_link = info.findAll(name='a', attrs='fixed-recipe-card__title-link').pop()
        recipe_name = title_link.findAll(name='span', attrs='fixed-recipe-card__title-link').pop().contents[0]
        if recipe_name not in recipe_names:
            recipe_names.append(recipe_name)
            
            # get recipe page
            attrs = title_link.attrs
            recipe_url = attrs['href']
            
            recipe_html = None
            recipe_soup = None
            try:
                recipe_html = request.urlopen(recipe_url)
                recipe_soup = bs(recipe_html, 'html.parser')
            except:
                continue # just skip it if there is an error reading the page

            # get ingredients
            ingredients = []
            ingred_spans = recipe_soup.findAll(name='span', attrs='recipe-ingred_txt added')
            if len(ingred_spans) == 0: # skip it if i don't know how to read the page
                print("skipping {0}".format(recipe_name))
                continue

            for i in range(len(ingred_spans)):
                span = ingred_spans.pop()
                ingred = span.contents[0]
                chars = [c.lower() for c in ingred if c not in remove_chars]
                ingred = ''.join(chars).strip()
                ingredients.append(ingred)

            # get recipe category
            category = ""
            ol = recipe_soup.findAll(name='ol', attrs='breadcrumbs breadcrumbs')
            if len(ol) > 0:
                ol = ol.pop()
                spans = ol.findAll(name='span', attrs='toggle-similar__title')
                category = spans.pop().contents[0].strip()
            else:
                print("skipping {0}".format(recipe_name))
                continue

            # add final recipe to recipes[]
            ingredients.append(category)
            recipes.append(ingredients)

# wow, done!
print("done!")

# give me some info!!!!
print("{0} pages read".format(page))
print("{0} recipes parsed".format(len(recipes)))

# write to a file
print("writing recipes to recipes.csv...")
with open('recipes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(recipes)

print("all done, goodnight and good luck")
