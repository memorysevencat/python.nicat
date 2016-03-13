#!/usr/bin/python2
#coding:utf-8
#copright by sevencat

class Car(object):
	country='china'
	def __init__(self,length,width,height,owner=None):
		self.__owner=owner
		self.length=length
		self.__width=width
		self.__height=height
	@property
	def owner(self):
	    return self._owner

	@owner.setter
	def owner(self,value):
		self._owner=value
	@owner.deleter
	def owner(self):
		self._owner=None

if __name__=='__main__':
	a=Car(1,2,3,'cat')
	print a.length
	#print a.__owner
	
