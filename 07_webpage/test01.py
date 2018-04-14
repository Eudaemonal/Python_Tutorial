#!/usr/bin/python3
import sys
import urllib.request


'''
Useage:
python3 test01.py http://www.google.com

'''

if __name__=="__main__":
    url = sys.argv[1] # supply url as first argument
    response = urllib.request.urlopen(url)
    content = response.read()
    print(content)
