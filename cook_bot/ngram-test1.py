# coding: utf-8
import pandas as pd
data = pd.read_csv("recipes.csv")
data.head()
data = pd.read_csv("recipes.csv", header=False)
data = pd.read_csv("recipes.csv", header=None)
data.head()
data.head()[0]
data.head()[1]
recipes = data[1]
recipes.head()
import nltk
from nltk import word_tokenize
recipes = [word_tokenize(r) for r in recipes]
recipes = [r.split(" ") for r in recipes]
recipes = [r.split(" ") for r in recipes]
recipes = data[1]
recipes = [r.split(" ") for r in recipes]
recipes = data[1]
recipes = [str(r).split(" ") for r in recipes]
recipes
len(recipes)
# that's a lot of recipes!
from nltk.util import ngrams
bigrams = ngrams(recipes, 2)
bigrams
trigrams = ngrams(recipes, 3)
fourgrams = ngrams(token, 4)
fourgrams = ngrams(recipes, 4)
fivegrams = ngrams(token, 5)
fivegrams = ngrams(recipes, 5)
bigrams
for grams in bigrams:
    print(grams)
    
fdist = nltk.FreqDist(recipes)
ingredients = [ingred for recipe in recipes for ingred in recipe]
freqdist = nltk.FreqDist(ingredients)
freqdist.most_common(10)
bigrams.send('a')
bigrams.send('TOMATO')
s = []
for n in range(0, 5):
    for bigram in bigrams:
        s.append(' '.join(str(i) for i in bigram))
        
s
s[0]
list(bigrams)
bigrams
bigrams.send('SPAGHETTI')
bigrams.send('A')
bigrams.send('TOMATO')
bigrams = ngrams(recipes, 2)
bigrams.send('TOMATO')
bigrams.send('TOMATO')
bigrams.send('TOMATO')
bigrams = ngrams(recipes, 2)
fdist2 = nltk.FreqDist(bigrams)
