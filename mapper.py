#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
import re

def format(word):
    #removes redundant symbols and converts to lowercase
    word = re.sub('[^a-zA-Z]+', '', word)
    word = word.lower()
    return word
# input comes from STDIN (standard input)
# check if line has content
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #check if line is not empty
    if line:
        # create dictionary of json
        loads = json.loads(line)
        # load tweet text to a variable
        text = loads["body"]
        #split text into words
        words = text.split()
        for word in words:
            #convert words to lowercase and removes non letters
            word = format(word)
            if word:
                # write the results to STDOUT (standard output);
                print(f"{word}\t{1}")