#!/usr/bin/python3
import sys


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__=="__main__":
    s1 = Singleton()
    print("First object", s1)

    s2 = Singleton()
    print("Second object", s2)

