#!/usr/bin/python3
import sys

'''
Run script using:

python3 test01.py < input01.txt

Note: "<" is a pipe that redirects the contents in file "input01.txt" to stdin
print() has a default '\n' that inserts a newline at the end
each line in the file also ends with '\n'

see the difference by uncomment: line = line.rstrip(), it removes '\n' from content
'''

if __name__=="__main__":
    for line in sys.stdin:
        # line = line.rstrip()
        print(line)


