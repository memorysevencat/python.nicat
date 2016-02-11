#!/usr/bin/env python
# coding:utf-8
#copyRight by sevencat

class PositiveNum(object):
	def __init__(self,value):
		self.val=value
	def __get__(self,instance,value):
		print '__get__',instance,value
		return self.val
	def __set__(self,instance,value):
		print '__set__',instance,value
		try:
			assert int(value)>0
			self.val=value
		except AssertionError:
			print 'Error '+str(value)+' is not positive number'
		except:
			print 'Error '+str(value)+' is not number'
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
	a=Car(10,12,15,'cat')
	b=Car(20,22,25,'cat')
	print a.length
	print b.length
	#class_object_2.py
