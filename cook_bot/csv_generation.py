# coding: utf-8
import csv
import nltk
recipes = []
with open(file='myrecipes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        recipes.append(row)
        
bigrams2d = [[bigrams for bigrams in list(nltk.ngrams(sequence=r, n=2))] for r in recipes]
flattened = []
for row in bigrams2d:
    for bigram in row:
        flattened.append(bigram)
        
bigram_fdist = nltk.FreqDist(flattened)
bigram_fdist.most_common(10)
bigram_fdist.most_common(15)
bigram_fdist.most_common(13)
false_bigrams = bigram_fdist.most_common(13)
first_words = []
second_words = []
for b, num in false_bigrams:
    first_words.append(b[0])
    second_words.append(b[1])
    
flattened2 = []
new_recipes = []
for r in recipes:
    new_recipe = []
    for i, ingredient in enumerate(r):
        if ingredient in first_words:
            index = first_words.index(ingredient)
            second_word = second_words[index]
            if i < len(r)-1 and r[i+1] == second_word:
                new_recipe.append("{0} {1}".format(ingredient, second_word))
            else:
                new_recipe.append(ingredient)
        else:
            new_recipe.append(ingredient)
    new_recipes.append(new_recipe)
    
new_recipes[101]
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
            if i < len(r)-1 and r[i+1] == second_word:
                new_recipe.append("{0} {1}".format(ingredient, second_word))
                false_bigram = True
            else:
                new_recipe.append(ingredient)
        else:
            new_recipe.append(ingredient)
    new_recipes.append(new_recipe)
    
new_recipes[101]
flattened2 = []
flattened
bigrams2d = [[bigrams for bigrams in list(nltk.ngrams(sequence=r, n=2))] for r in recipes]
new_bigrams2d = [[bigrams for bigrams in list(nltk.ngrams(sequence=r, n=2))] for r in new_recipes]
new_bigrams2d
flattened2 = []
for row in new_bigrams2d:
    for b in row:
        flattened2.append(b)
        
bigrams_freqdist2 = nltk.FreqDist(flattened2)
bigrams_freqdist2.most_common(5)
import pickle
with open(file='bigrams_freqdist', mode='wb') as outfile:
    pickle.dump(bigrams_freqdist2, outfile)
    
bigram_data = []
for key in bigrams_freqdist2.keys():
    freq = freqdist2.freq(key)
    w1 = key[0]
    w2 = key[1]
    
for key in bigrams_freqdist2.keys():
    freq = bigrams_freqdist2.freq(key)
    w1 = key[0]
    w2 = key[1]
    data.append([w1, w2, freq])
    
for key in bigrams_freqdist2.keys():
    freq = bigrams_freqdist2.freq(key)
    w1 = key[0]
    w2 = key[1]
    bigram_data.append([w1, w2, freq])
    
with open(file='bigram_freqs.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
    
with open(file='bigram_freqs.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(bigram_data)
    
    
new_recipes
with open(file='bigram_corrected_recipes.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(new_recipes)
    
trigrams2d = [[trigrams for trigrams in list(nltk.ngrams(sequence=r, n=3))] for r in new_recipes]
flattened = []
for row in trigrams2d:
    for trigram in row:
        flattened.append(trigram)
        
flattened[0]
trigram_fdist = nltk.FreqDist(flattened)
trigram_fdist.most_common(5)
# nothing that can be really separated there, save and move on
with open(file='trigram_fdist', mode='wb') as outfile:
    pickle.dump(trigram_fdist, outfile)
    
trigram_data = []
for key in trigram_fdist.keys():
    freq = trigram_fdist.freq(key)
    w1 = key[0]
    w2 = key[1]
    w3 = key[3]
    trigram_data.append([w1, w2, w3, freq])
    
for key in trigram_fdist.keys():
    freq = trigram_fdist.freq(key)
    w1 = key[0]
    w2 = key[1]
    w3 = key[2]
    trigram_data.append([w1, w2, w3, freq])
    
trigram_data
with open(file='trigram_freqs.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(trigram_data)
    
len(trigram_data)
