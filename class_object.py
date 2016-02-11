#!/usr/bin/env python
# coding:utf-8
#copyRight by sevencat

class PositiveNum(object):
	def __init__(self,value):
		self.val=value
	def __get__(self,instance,owner):
		print '__get__',instance,owner
		return self.val
	def __set__(self,instance,value):
		print '__set__',instance,value
		try:
			assert int(value)>0
			self.val=value
		except AssertionError:
			print 'Error '+str(value)
		except:
			print 'Error '+str(value)
	def __delete__(self,instance):
		print '__delete__',instance
		self.val=None
class Car(object):
	country = 'cn'
	length=PositiveNum(0)
	width=PositiveNum(0)
	height=PositiveNum(0)

	def __init__(self,length,width,height,owner=None):
		self.owner=owner
		self.length=length
		self.width=width
		self.height=height

if __name__=='__main__':
	a=Car(10,12,'cat')

	#print a.owner
	#del a.owner
	#print a.owner
	#print a.name
