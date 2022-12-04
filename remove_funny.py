#!/usr/bin/env python

import sys

def remove_funny(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    with open(file_name, 'w') as f:
        for line in lines:
            if line.strip() != sys.argv[1]:
                f.write(line)

if __name__ == '__main__':
    remove_funny('funny.txt')
