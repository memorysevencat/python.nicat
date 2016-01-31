#!/usr/bin/env python
# coding:utf-8

import random

def part_func(list,start,end):
	flag=list[end]
	i=start-1
	for j in range(start,end):
		if list[j] <= flag:
			i+=1
			list[i],list[j]=list[j],list[i]
	list[i+1],list[end]=list[end],list[i+1]
	return i+1

def quick_sort_inner(list,start,end):
	if start >=end :
		return
	size=part_func(list,start,end)
	quick_sort_inner(list,start,size-1)
	quick_sort_inner(list,size+1,end)

def quick_sort(list):
	quick_sort_inner(list,0,len(list)-1)

def creat_list(n):
	return  [random.randint(1,100) for i in range(n)]

if __name__=='__main__':
	n=10
	list=creat_list(n)
	print list
	quick_sort(list)
	print list
