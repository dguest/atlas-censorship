#!/usr/bin/env python3

from json import load

with open('nothing.json') as very_bad:
    badwords = load(very_bad)

with open('atlas-nolike.txt') as atlas_no:
    word_numbers = {int(x)-1 for x in atlas_no.read().split()}

for number, word in enumerate(badwords):
    if number not in word_numbers:
        print(word)
