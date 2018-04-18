#!/usr/bin/python3
import sys
import re
from collections import defaultdict



if __name__=="__main__":
    count=defaultdict(int)
    f=open('input01.txt')
    for line in f:
        for word in re.findall(r'\w+',line.lower()):
            count[word]+=1
    words=list(count.keys())
    sorted_words=sorted(words, key=lambda w:count[w])
    for word in sorted_words:
        print("{} {}".format(count[word], word))
