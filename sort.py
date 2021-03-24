#!/usr/bin/env/python3

import os

def get_key (dicts, value):
    return [k for k, v in dicts.items() if v == value]

path = os.getcwd()
file = 'part-00000'
words = {}
with open(os.path.join(path,file),'r') as f:
    for line in f:
        if line.strip().split()[1]:
            words[line.strip().split()[1]] = int(line.strip().split()[0])
word_list = list(words.values())
word_list.sort(reverse=True)

a = word_list[:15]
print(a)
for word in a:
    print(word, get_key(words, word))
    
            

