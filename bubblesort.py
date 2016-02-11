#!/usr/bin/python2
# coding:utf-8

import random

def bubble(list):
	for i in range(len(list),-1,-1):
		for j in range(0,i-1,1):
			if list[j] > list[j+1]:
				list[j],list[j+1]=list[j+1],list[j]

if __name__=='__main__':
	list=[random.randint(1,100)  for i in range(10)]
	print list
	bubble(list)
	print list
