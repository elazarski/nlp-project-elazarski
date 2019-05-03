# coding: utf-8
import csv
data = []
with open(file='recipes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        data.append(row)
        
data[0]
recipes = [str(row[1]).split(" ") for row in data]
recipes[0]
with open(file='myrecipes.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
    
with open(file='myrecipes.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(recipes)
    
