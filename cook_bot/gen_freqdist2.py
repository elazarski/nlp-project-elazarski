# coding: utf-8
import csv
recipes = []
with open(file='myrecipes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        recipes.append(row)
        
recipes[0]
import nltk
bigrams(recipes)
fdist = nltk.FreqDist([bigrams for bigrams in list(nltk.ngrams(sequence=recipe, n=2)) for recipe in recipes])
[bigrams for bigrams in list(nltk.ngrams(r, n=2)) for r in recipes]
[bigrams for bigrams in list(nltk.ngrams(r, n=2))] for r in recipes]
[[bigrams for bigrams in list(nltk.ngrams(r, n=2))] for r in recipes]
nltk.FreqDist([[bigrams for bigrams in list(nltk.ngrams(r, n=2))] for r in recipes])
nltk.FreqDist([[bigrams for bigrams in list(nltk.ngrams(r, n=2))] for r in recipes].flatten())
bigrams2d = [[bigrams for bigrams in list(nltk.ngrams(sequence=r, n=2))] for r in recipes]
bigrams2d[0]
freqdist = nltk.FreqDist([bigrams for bigrams in bigrams2d])
flattenedbigrams = [t for t in bigrams for bigrams in bigrams2d]
import numpy as np
flattened = np.ndarray.flatten(bigrams2d)
flattened = np.ndarray.flatten(np.ndarray(bigrams2d))
flattened = []
for row in bigrams2d:
    recipe = ['<START>']
    for ingredient in recipe:
        recipe.append(ingredient)
    recipe.append('<END>')
    flattened.append(recipe)
    
flattened = []
for row in bigrams2d:
    recipe = ['<START>']
    for ingredient in row:
        recipe.append(ingredient)
    recipe.append('<END>')
    flattened.append(recipe)
    
freqdist = nltk.FreqDist(flattened)
flattened[0]
flattened
flattened = []
for row in bigrams2d:
    flattened.append('<START>')
    for i in row:
        flattened.append(i)
    flattened.append('<END>')
    
    
freqdist - nltk.FreqDist(flattened)
freqdist = nltk.FreqDist(flattened)
freqdist.most_common()
freqdist.most_common(5)
freqdist.most_common(10)
freqdist.most_common(20)
freqdist.most_common(17)
freqdist.most_common(15)
flattened2 = []
false_bigrams = freqdist.most_common(15)
false_bigrams[1]
false_bigrams.remove(0)
false_bigrams
false_bigrams.remove(tuple('<END>', 74839))
false_bigrams.remove(zip('<END>', 74839))
false_bigrams.remove(('<END>', 74839))
false_bigrams
false_bigrams.remove(('<START>', 74839))
false_bigrams
first_words = [first for first,second in false_bigrams]
second_words = [second for first,second in false_bigrams]
first_words
second_words
first_words = [first first,second in dist for dist in false_bigrams]
first_words = [first for first,second in dist for dist in false_bigrams]
first_words = [[first for first,second in dist] for dist in false_bigrams]
first_words = [[first for first,second in t] for t,num in false_bigrams]
first_words = [first for first,second in t for t,num in false_bigrams]
first_words = []
second_words = []
for t, num in false_bigrams:
    for first, second in t:
        first_words.append(first)
        second_words.append(second)
        
for t, num in false_bigrams:
    print(t)
    
for t, num in false_bigrams:
    print(t[0])
    
for t, num in false_bigrams:
    first_words.append(t[0])
    second_words.append(t[1])
    
first_words
second_words
flattened2 = []
flattened[0]
flattened[1]
first_words.index('OIL')
first_words.index('a')
for bigram in flattened:
    if first_words.contains(bigram[0])
flattened[2]
recipes[0]
false_bigrams
for r in recipes:
    new_recipe = []
    for i, ingredient in enumerate(r):
        if ingredient in first_words:
            index = first_words.index(ingredient)
            second_word = second_words[index]
            if i < len(r)-1 and r[i + 1] == second_word:
                new_recipe.append("{0} {1}".format(ingredient, second_word))
            else:
                new_recipe.append(ingredient)
        else:
            new_recipe.append(ingredient)
            
new_recipes = []
for r in recipes:
    new_recipe = []
    for i, ingredient in enumerate(r):
        if ingredient in first_words:
            index = first_words.index(ingredient)
            second_word = second_words[index]
            if i < len(r)-1 and r[i + 1] == second_word:
                new_recipe.append("{0} {1}".format(ingredient, second_word))
            else:
                new_recipe.append(ingredient)
        else:
            new_recipe.append(ingredient)
    new_recipes.append(new_recipe)
    
new_recipes[100]
new_recipes[101]
flattened2 = []
for r in new_recipes:
    flattened2.append('<START>')
    for i in r:
        flattened2.append(i)
    flattened2.append('<END>')
    
freqdist2 = nltk.FreqDist([bigram for bigram in nltk.ngrams(sequence=flattened2, n=2)])
freqdist2.most_common(5)
new_recipes = []
for r in recipes:
    new_recipe = []
    false_bigram = False
    for i, ingredient in enumerate(r):
        if false_bigram:
            false_bigram = False
            continue
        if ingredient in first_words:
            index = first_words.index(ingredient)
            second_word = second_words[index]
            if i < len(r)-1 and r[i + 1] == second_word:
                new_recipe.append("{0} {1}".format(ingredient, second_word))
                false_bigram = True
            else:
                new_recipe.append(ingredient)
         else:
            new_recipe.append(ingredient)
    new_recipes.append(new_recipe)
    
for r in recipes:
    new_recipe = []
    false_bigram = False
    for i, ingredient in enumerate(r):
        if false_bigram:
            false_bigram = False
            continue
        if ingredient in first_words:
            index = first_words.index(ingredient)
            second_word = second_words[index]
            if i < len(r)-1 and r[i + 1] == second_word:
                new_recipe.append("{0} {1}".format(ingredient, second_word))
                false_bigram = True
            else:
                new_recipe.append(ingredient)
        else:
            new_recipe.append(ingredient)
    new_recipes.append(new_recipe)
    
flattened2 = []
for r in new_recipes:
    flattened2.append('<START>')
    for i in r:
        flattened2.append(i)
    flattened2.append('<END>')
    
flattened2[101]
new_recipes[101]
freqdist2 = nltk.FreqDist([bigram for bigram in nltk.ngrams(sequence=flattened2, n=2)])
freqdist2.most_common(5)
for f in freqdist2:
    print(f)
    
for f,num in freqdist2:
    print(f)
    
freqdist2
import pickle
with open(file='freqdist2', mode='wb') as outfile:
    pickle.dump(freqdist2)
    
with open(file='freqdist2', mode='wb') as outfile:
    pickle.dump(freqdist2, outfile)
    
    
