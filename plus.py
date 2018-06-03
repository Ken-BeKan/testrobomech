#! /usr/lib/python3
# -*- coding: utf-8 -*-

def plus(a,b):
    return a+b

if __name__ == '__main__':
    import sys

    if plus(1,2)!=3:
        sys.exit(1)

    if plus (1.1, 2.2) < 3.299999 or plus(1.1, 2.2) > 3.300001:
        sys.exit(2)

    if plus("abc", "def") != "abcdef":
        sys.exit(3)

    sys.exit(0)
