#!/usr/bin/python2
# coding:utf-8

import itertools

l=[1,2,3,4]
r=itertools.permutations(l)

a=itertools.product([1,2],[3,4])
b=itertools.repeat([1,2],4)

c=itertools.chain(r,a,b)

print [i for i in c]
