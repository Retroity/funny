#!/usr/bin/env python

import sys

def make_funny(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    with open(file_name, 'w') as f:
        for line in lines:
            if line.strip() == sys.argv[1]:
                f.write(line.replace(sys.argv[1], 'funny'))
            else:
                f.write(line)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        make_funny('funny.txt')
    else:
        print("Please provide a string to replace")
