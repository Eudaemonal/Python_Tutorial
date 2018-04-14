#!/usr/bin/python3
import sys


'''
Run script using:
python3 test01.py < input01.txt

'''

if __name__=="__main__":
    for line in sys.stdin:
        line = line.rstrip()

        # split the string by white space and convert it to a list
        words = line.split()
        print(words)
