#!/usr/bin/python3
import sys
import time
from functools import reduce
from math import sqrt, exp, log, sin, cos, pi
from collections import defaultdict


# pseudo-random number generator 
# Implemented as: X = (a*X + b) mod m
class random:
    # LGM method
    def __init__(self):
        self.m = 0x7fffffff 
        self.a = 0x41a7
        self.b = 0

        self.normal_flag = 0

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

    # exponential distribution
    def exponential(self, lamda):
        return -lamda * log(1 - self.randomfloat(0,1))

    # normal distribution Box-Muller method
    def normal(self):
        if self.normal_flag==1: 
            self.normal_flag = 0
        else:
            self.normal_flag = 1
            u1 = self.randomfloat(0,1)
            u2 = self.randomfloat(0,1)
            self.z1 = sqrt(-2*log(u1)) * cos(2*pi*u2)
            self.z2 = sqrt(-2*log(u1)) * sin(2*pi*u2) 
        
        if self.normal_flag==1: 
            return self.z1
        else: 
            return self.z2

if __name__=="__main__":
    # generate exponential distribution
    m1 = random()
    m1.seed(1)
    print(m1.exponential(1.5))

    # generate 5000 normal distribution
    m2 = random()
    m2.seed(1)
    z = []
    for i in range(0,5000):
        z.append(m2.normal())


    #empirical mean
    mean = reduce(lambda x, y: x + y, z) / len(z)
    #empirical standard deviation
    sd = sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2,z))) / (len(z)-1))

    print(mean)
    print(sd)
