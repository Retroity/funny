#!/usr/bin/env python

import random

def make_funny(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    print(random.choice(lines))

if __name__ == '__main__':
    make_funny('funny.txt')
