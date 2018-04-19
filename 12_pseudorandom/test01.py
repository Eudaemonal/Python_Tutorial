#!/usr/bin/python3
import sys
import time
from functools import reduce
from math import sqrt


# pseudo-random number generator 
# Implemented as: X = (a*X + b) mod m
class random:
    # LGM method
    def __init__(self):
        self.m = 0x7fffffff 
        self.a = 0x41a7
        self.b = 0

    # set seed to start with
    def seed(self, s):
        self.seed = s
        self.x = s
    
    # generate pseudorandom number
    def random(self):
        self.x = (self.a * self.x + self.b) % self.m
        return self.x

    # generate random int between lower and upper bound
    def randomint(self, lower, upper):
        assert upper > lower
        self.x = (self.a * self.x + self.b) % self.m
        return self.x % (upper + 1 - lower) + lower

    # generate random float between lower and upper bound
    def randomfloat(self, lower, upper):
        assert upper > lower
        self.x = (self.a * self.x + self.b) % self.m
        return (float)(self.x/self.m)*(upper - lower) + lower


if __name__=="__main__":
    # use 1 as seed
    m1 = random()
    m1.seed(1)
    print(m1.random())

    # use time as seed
    m2 = random()
    m2.seed(int(time.time()))
    print(m2.random())

    # generate 10000 uniformly distributed random number on [0,1]
    m3 = random()
    u = []
    m3.seed(1)
    for i in range(0,10000):
        u.append(m3.randomfloat(0,1))
    
    #empirical mean
    mean = reduce(lambda x, y: x + y, u) / len(u)
    #empirical standard deviation
    sd = sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2,u))) / (len(u)-1))
    
    print(mean)
    print(sd)
