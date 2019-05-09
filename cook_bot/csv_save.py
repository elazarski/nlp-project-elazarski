# coding: utf-8
import csv
# the original file contains URLs and the ingredient lists are split by space, convert that to CSV
data = []
with open(file='recipes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        data.append(row)
        
recipes = [str(row[1]).split(" ") for row in data]    
with open(file='myrecipes.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(recipes)
    
