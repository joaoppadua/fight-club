#! python3
"""
Created on Mon Sep 24 18:34:47 2018

@author: João Pedro
"""

# script for concordancing native texts

import nltk, os

def find(name, path='c:\\Users'):
    for root, dirs, files in os.walk(path):
        if name in files:
            return(os.path.join(root, name))

name = input('enter file name: ')

#print(find(name))

with open(find(name), 'r') as f:
    raw = f.read()

tokens = nltk.wordpunct_tokenize(raw)
clean_tokens = [word.lower() for word in tokens if word.isalpha()]

text = nltk.Text(clean_tokens)
print(len(text))
text.concordance(input('enter word: '), width=6, lines=30)
print(text.collocations())

