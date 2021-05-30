import json
import os
from collections import Counter
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

files = os.listdir('Dataset')
dictionary = {}

with open("Dictionary.json", 'r') as dump:
    dictionary = json.loads(dump.read())

def text_to_seq(text_sample):
    char_to_idx = dictionary
    idx_to_char = {v: k for k, v in char_to_idx.items()}
    sequence = np.array([char_to_idx[char] for char in text_sample])
    
    return sequence, char_to_idx, idx_to_char

def get_batch():
    SEQ_LEN = 64
    BATCH_SIZE = 16
    
    trains = []
    targets = []

    for _ in range(BATCH_SIZE):
        file = files[np.random.randint(0, len(files))]
        text = ''

        while len(text) < SEQ_LEN:
            text = ''
            with open("file", 'r') as f:
                for line in f:
                    text = text + line + '\n'

        sequence, _, __ = text_to_seq(text)

        batch_start = np.random.randint(0, len(sequence) - SEQ_LEN)
        chunk = sequence[batch_start: batch_start + SEQ_LEN]
        train = torch.LongTensor(chunk[:-1]).view(-1, 1)
        target = torch.LongTensor(chunk[1:]).view(-1, 1)
        trains.append(train)
        targets.append(target)

    return torch.stack(trains, dim=0), torch.stack(targets, dim=0)