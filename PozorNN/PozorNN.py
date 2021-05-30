import json
import os
from collections import Counter
import numpy as np

#files = os.listdir('Dataset')
dictionary = {}

with open("Dictionary.json", 'r') as dump:
    dictionary = json.loads(dump.read())

def text_to_seq(text_sample):
    char_counts = Counter(text_sample)
    char_counts = sorted(char_counts.items(), key = lambda x: x[1], reverse=True)

    sorted_chars = [char for char, _ in char_counts]
    print(sorted_chars)
    char_to_idx = dictionary
    idx_to_char = {v: k for k, v in char_to_idx.items()}
    sequence = np.array([char_to_idx[char] for char in text_sample])
    
    return sequence, char_to_idx, idx_to_char

sec, _, __ = text_to_seq("Отдыхаю я значит")

print(sec)