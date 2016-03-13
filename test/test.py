#!/usr/bin/python2
# coding:utf-8
import random
import time

def time_cost(f):
	def  dec(func):
		def _f(*arg,**kwrg):
			start=f()
			func(*arg,**kwrg)
			end=f()
			print end-start
		return _f
	return dec

@time_cost(time.time)
def func_one(length):
	return  [(x,y) for x in range(length) for y in range(length) if x*y >50]

@time_cost(time.time)
def func_two(length):
	result=[]
	for x in range(length):
		for y in range(length):
			if x*y > 50:
				result.append((x,y))
	return result

if __name__=="__main__":
	pass
	func_one(1000)
	print '#'
	func_two(1000)
