# -*- coding: utf-8 -*-
import re

def word_count(text):
    words = re.sub('[,._:!&@$%^🖖]+', ' ', text).split()
    word_count = {}
    for word in words:
        if decode_if_needed(word.lower()) in word_count:
            word_count[decode_if_needed(word.lower())] += 1
        else:
            word_count[decode_if_needed(word.lower())] = 1
    return word_count

def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string
