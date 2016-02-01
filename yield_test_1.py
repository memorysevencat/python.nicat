#!/usr/bin/env python
# coding:utf-8
import random
import time

def fib_opt(n):
	a,b,i=0,1,0
	while i < n:
		a,b=b,a+b
		i+=1
	else:
		return b

def fib_iter():
	a,b=0,1
	while True:
		yield b
		a,b=b,a+b

if __name__=='__main__':
	start=time.clock()
	f=fib_iter()
	iter_func=[f.next() for i in range(1000)]
	end=time.clock()
	print end-start

	start=time.clock()
	opt_func=[fib_opt(i) for i in range(1000)]
	end=time.clock()
	print end-start
	if opt_func==iter_func:
		print True
	else:
		print False
