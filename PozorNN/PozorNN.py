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

char_to_idx = dictionary
idx_to_char = {v: k for k, v in char_to_idx.items()}

def text_to_seq(text_sample):
    sequence = np.array([char_to_idx[char] for char in text_sample])
    
    return sequence

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

        sequence = text_to_seq(text)

        batch_start = np.random.randint(0, len(sequence) - SEQ_LEN)
        chunk = sequence[batch_start: batch_start + SEQ_LEN]
        train = torch.LongTensor(chunk[:-1]).view(-1, 1)
        target = torch.LongTensor(chunk[1:]).view(-1, 1)
        trains.append(train)
        targets.append(target)

    return torch.stack(trains, dim=0), torch.stack(targets, dim=0)

def evaluate(model, char_to_idx, idx_to_char, start_text=' ', prediction_len=200, temp=0.3):
    hidden = model.init_hidden()
    idx_input = [char_to_idx[char] for char in start_text]
    train = torch.LongTensor(idx_input).view(-1, 1, 1).to(device)
    predicted_text = start_text
    
    _, hidden = model(train, hidden)
        
    inp = train[-1].view(-1, 1, 1)
    
    for i in range(prediction_len):
        output, hidden = model(inp.to(device), hidden)
        output_logits = output.cpu().data.view(-1)
        p_next = F.softmax(output_logits / temp, dim=-1).detach().cpu().data.numpy()        
        top_index = np.random.choice(len(char_to_idx), p=p_next)
        inp = torch.LongTensor([top_index]).view(-1, 1, 1).to(device)
        predicted_char = idx_to_char[top_index]
        predicted_text += predicted_char
    
    return predicted_text