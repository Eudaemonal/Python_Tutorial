#!/usr/bin/python3
import sys

if __name__=="__main__":
    v = [] # create empty list
    for line in sys.stdin:
        line = line.rstrip()
        v.append(int(line)) # convert line to int and append to list
        
    v.sort() # sort the list
    print(v)
