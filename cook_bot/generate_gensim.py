# coding: utf-8
import gensim
import csv

# read recipes and generate a word2vec model from them
recipes = []
with open('bigram_corrected_recipes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        recipes.append(row)
        
recipes[0]
model = gensim.models.Word2Vec(recipes)
model.wv.similarity('EGG', 'CHICKEN')
model.wv.most_similar(positive=['EGG'], topn=3)

# save the model
import pickle
with open('gensim_model', mode='wb') as outfile:
    pickle.dump(model, outfile)
    
