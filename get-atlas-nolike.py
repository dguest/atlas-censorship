#!/usr/bin/env python3

from json import load

with open('nothing.json') as very_bad:
    badwords = load(very_bad)

with open('atlas-nolike.txt') as atlas_no:
    word_number = [int(x)-1 for x in atlas_no.read().split()]

for word in word_number:
    print(badwords[word])
