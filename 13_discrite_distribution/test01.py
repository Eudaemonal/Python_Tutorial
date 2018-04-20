#!/usr/bin/python3
import sys
import time
from functools import reduce
from math import sqrt, exp
from collections import defaultdict


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
    
    # generate bernoulli distribution
    def bernoulli(self, p):
        assert p > 0.0
        assert p < 1.0
        u = self.randomfloat(0,1)
        if(u < p):
            return 1
        else: 
            return 0

    # generate binomial distribution
    def binomial(self, n, p):
        assert n > 0
        s = 0
        for i in range(0, n):
            s += self.bernoulli(p)
        return s

    # generate poisson distribution
    def poisson(self):
        return

if __name__=="__main__":

    # count 0 and 1 in bernoulli distribution
    m1 = random()
    m1.seed(1)

    count = defaultdict(int)
    for i in range(0,10000):
        count[m1.bernoulli(0.2)]+=1

    nums=list(count.keys())
    for num in nums:
        print("{}: {}".format(num, count[num]))

    # count numbers in binomial distribution
    m2 = random()
    m2.seed(1)
    count = defaultdict(int)
    for i in range(0,1000):
        count[m2.binomial(44, 0.64)]+=1

    nums=list(count.keys())
    sorted_nums = sorted(nums, key=lambda n:n)
    for num in sorted_nums:
        print("{}: {}".format(num, count[num]))


