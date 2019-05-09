# coding: utf-8
# this worked better for bigram frequencies, but i prettied it up for final use
import nltk
import pickle
with open(file='freqdist2', mode='rb') as infile:
    freqdist2 = pickle.load(infile)
    
freqdist2.most_common(5)
l = list(freqdist2)
l[0]
'BONE' in  l
'BONE' in  l[0]
l
freqdist2
freqdist2.freq(sample='FISH')
freqdist2.freq(sample=('FISH', 'FILET'))
freqdist2.items
freqdist2.items()
import pandas as pd
datafram = pd.DataFrame(columns=['w1', 'w2', 'num'])
dataframe = pd.DataFrame(columns=['w1', 'w2', 'num'])
freqdist2.items()[0]
freqdist2.items()
freqdist2.keys()
freqdist2.elements
freqdist2.elements()
for element in freqdist2.elements():
    print(element)
    
freqdist2.values()
freqdist2.keys()
for key in freqdist2.keys():
    num = freqdist2.freq(key)
    w1 = key[0]
    w2 = key[2]
    dataframe.append([w1, w2, num])
    
for key in freqdist2.keys():
    num = freqdist2.freq(key)
    w1 = key[0]
    w2 = key[1]
    dataframe.append([w1, w2, num])
    
data = []
for key in freqdist2.keys():
    num = freqdist2.freq(key)
    w1 = key[0]
    w2 = key[1]
    data.append([w1, w2, num])
    
    
ignore_symbols = ['<START>', '<END>']
for key in freqdist2.keys():
    num = freqdist2.freq(key)
    w1 = key[0]
    w2 = key[1]
    
    if not (w1 in ignore_symbols or w2 in ignore_symbols):
        data.append([w1, w2, num])
        
data
data = []
for key in freqdist2.keys():
    num = freqdist2.freq(key)
    w1 = key[0]
    w2 = key[1]
    
    if not (w1 in ignore_symbols or w2 in ignore_symbols):
        data.append([w1, w2, num])
        
data
import csv
with open(file='frequencies.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
    
