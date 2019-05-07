#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:17:41 2019

@author: eric lazarski
this program takes the models generated in the other Python files
and uses it to generate recipes. Have fun and get cooking!
"""

# imports
import pickle
import random
import pandas as pd
from nltk.corpus import wordnet as wn

# read necessary files
bigram_freqs = pd.read_csv('bigram_freqs.csv', header=None)
trigram_freqs = pd.read_csv('trigram_freqs.csv', header=None)
gensim_model = None
with open(file='gensim_model', mode='rb') as infile:
    gensim_model = pickle.load(infile)
    
# global variables
generated_recipe = False
starting_ingredients = []
recipe = []
    
# functions
# add a starting ingredient
def add_ingredient():
    global starting_ingredients
    global recipe
    
    ingredient = input("Enter an ingredient: ").upper()
    starting_ingredients.append(ingredient)
    
# clear global variables
def clear_vars():
    global starting_ingredients
    global recipe
    
    starting_ingredients = []
    recipe = []
    
# return lemmas for an ingredient
# ...hopefully we have one of those...
def get_lemmas(ingredient):
    lemmas = []
    synsets = wn.synsets(ingredient)
    if len(synsets) == 0:
        print("I'm sorry, I don't know anything about {0}".format(ingredient))
        return None
    
    # get all of the possible lemmas and send that back
    for s in synsets:
        for l in s.lemma_names():
            lemmas.append(l.upper())
    
    # remove duplucates
    return set(lemmas)
    
def gen_next_ingredient_bigram(prev_ingredient):
    global bigram_freqs
    
    # get combinations that contain the previous ingredient
    filter1 = bigram_freqs[0] == prev_ingredient
    bigrams = bigram_freqs.where(filter1, inplace=False).dropna()
    
    # if nothing was found, try a synonym of the ingredient
    if len(bigrams) == 0:
        lemmas = get_lemmas(prev_ingredient)
        for l in lemmas:
            filter1 = bigram_freqs[0] == l
            bigrams = bigram_freqs.where(filter1, inplace=False).dropna()
            if len(bigrams) > 0:
                break
            return None # nothing found :(
    
    # return a random choice from the best ingredients
    prob = sorted(bigrams[2].unique(), reverse=True)[0]
    filter2 = bigrams[2] == prob
    bigrams = bigrams.where(filter2, inplace=False).dropna()
    best_ingredients = list(bigrams[1])
    
    return random.choice(best_ingredients)
    
    
def gen_next_ingredient_trigram(prev_ingredient, prevprev_ingredient):
    global trigram_freqs
    filter1 = trigram_freqs[0] == prev_ingredient
    filter2 = trigram_freqs[1] == prevprev_ingredient
    # get combinations that contain the first two ingredients
    trigrams = trigram_freqs.where(filter1 & filter2, inplace=False).dropna()
    
    # if nothing was found, backoff to bigrams
    if len(trigrams) == 0:
        return gen_next_ingredient_bigram(prev_ingredient)
    
    # pick the most probable third ingredient, if they are equal, pick a random one
    prob = sorted(trigrams[3].unique(), reverse=True)[0]
    filter3 = trigrams[3] == prob
    trigrams = trigrams.where(filter3, inplace=False).dropna()
    best_ingredients = list(trigrams[2])
    
    return random.choice(best_ingredients)
    
# generates the next ingredient
def gen_next_ingredient():
    global recipe
    
    # use trigrams if available, otherwise default to bigrams
    if len(recipe) > 3:
        # use trigrams
        prev_ingredient = recipe[-1]
        prevprev_ingredient = recipe[-2]
        return gen_next_ingredient_trigram(prev_ingredient, prevprev_ingredient)
    else:
        # use bigrams
        prev_ingredient = recipe[-1]
        return gen_next_ingredient_bigram(prev_ingredient)
        

# use gensim model to get a similar ingredient
def replace_ingredient(ingredient):
    global gensim_model
    
    # how many ingredients does the user want?
    num_replacements = input("Enter how many options to generate: ")
    while not num_replacements.isdigit():
        print("That wasn't a number...")
        num_replacements = input("Enter how many options to generate: ")
    
    num_replacements = int(num_replacements)
    replacements = gensim_model.wv.most_similar(positive=[ingredient],
                                                topn=num_replacements)
    replacements = sorted(replacements, key=lambda tup: tup[1], reverse=True)
    
    # give the user a choice
    print("Here are your options sorted by similarity:")
    for i, choice in enumerate(replacements):
        print("{0}. {1}".format(i, choice[0]))
    
    choice = input("Enter the number of your choice: ")
    while not choice.isdigit() or int(choice) > len(replacements):
        print("That isn't an option...")
        choice = input("Enter the number of your choice: ")
    
    return replacements[int(choice)][0]

# generate a complete ingredient list
def gen_ingredient_list():
    global generated_recipe
    global starting_ingredients
    global recipe
    
    num_ingredients = input("Enter how many ingredients to generate: ")
    while not num_ingredients.isdigit():
        print("That wasn't a number...")
        num_ingredients = input("Enter how many ingredients to generate: ")
    
    recipe = starting_ingredients    
    while len(recipe) < int(num_ingredients):
        recipe.append(gen_next_ingredient())   
        
    generated_recipe = True

# print a simple menu
def menu():
    global generated_recipe
    
    print("--------------------------------------------------------------------------------")
    print("Menu:")
    print("1. Enter starting ingredient")
    print("2. Generate ingredient list")
    print("3. Replace a returned ingredient")
    print("4. Start over")
    print("5. Exit")
    
    if generated_recipe:
        print("")
        print("Here is your recipe:")
        print(recipe)
    
    response = input("Enter a number: ")
    while (not response.isdigit()) or (int(response) < 1 or int(response) > 5):
        print("That is not an option!")
        response = input("Enter a number: ")

    return int(response)

# parse user response
def parse_response(response):
    if response == 1:
        # add an ingredient
        add_ingredient()
    elif response == 2:
        # generate ingredient list based on how many ingredients the user wants
        if len(starting_ingredients) > 0:
            gen_ingredient_list()
            
            print(recipe)
        else:
            print("Give me something to start with first!")
    elif response == 3:
        if len(recipe) == 0:
            print("Generate a recipe first!")
        else:
            # use gensim to get most similar ingredients
            ingredient = input("Enter an ingredient to replace: ").upper()
            if ingredient not in recipe:
                print("{0} is not in your recipe!")
            else:
                new_ingredient = replace_ingredient(ingredient)
                index = recipe.index(ingredient)
                recipe[index] = new_ingredient                
    elif response == 4:
        # clear global variables
        clear_vars()
        
# main loop
response = menu()
while response != 5:
    parse_response(response)
    response = menu()
    
print("Goodbye!")
exit()