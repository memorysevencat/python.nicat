#!/usr/bin/python2
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
mem_cache={}
def mem_fib(n):
	if n not in mem_cache.keys():
		if n<=2:
			mem_cache[n]=1
		else:
			mem_cache[n]=fib(n-1)+fib(n-2)
	return mem_cache[n]

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
		
	nlist=[random.randint(1,30) for i in range(100)]
	fib_func_result=[]
	fib_func=[mem_fib(i) for i in nlist]
	for i in nlist:
		fib_func_result.append(mem_cache[i])
	print fib_func_result
