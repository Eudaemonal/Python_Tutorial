#!/usr/bin/python3
import sys
from functools import reduce
from math import sqrt


'''
Least square method:
y = b0 + b1 * t

b0 = y_ - b1 * t_
b1 = cov(t, y)/ var(t)


'''

if __name__=="__main__":
    i = 0
    t = []
    y = []
    for line in sys.stdin:
        if(i==0):
            size = int(line)
        if(i!=0):
            a, b = line.split()
            t.append(float(a))
            y.append(float(b))
        i+=1

    t_ = reduce(lambda x, y: x + y, t)/len(t)
    y_ = reduce(lambda x, y: x + y, y)/len(y)

    print(t_)
    print(y_)

    b1_upper = 0
    b1_lower = 0
    for i in range(0, size):
        b1_upper += (t[i] - t_)*(y[i] - y_)
        b1_lower += (t[i] - t_)**2
        
    b1 = b1_upper/ b1_lower

    b0 = y_ - b1 * t_;
    print(b1)
    print(b0)
