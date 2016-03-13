#!/usr/bin/python2
# coding:utf-8
#copyRight by sevencat

class PositiveNum(object):
	def __init__(self):
		self.default=None
		self.data={}
	def __get__(self,instance,value):
		print '__get__',instance,value
		return self.data.get(instance,self.default)
	def __set__(self,instance,value):
		print '__set__',instance,value
		try:
			assert int(value)>0
			self.data[instance]=value
		except AssertionError:
			print 'Error '+str(value)+' is not positive number'
		except:
			print 'Error '+str(value)+' is not number'
	def __delete__(self,instance):
		print '__delete__',instance
		del self.data[instance]
class Car(object):
	country = 'cn'
	length=PositiveNum()
	width=PositiveNum()
	height=PositiveNum()
	__slots__=('owner','length','width','height')
	def __init__(self,length,width,height,owner=None):
		self.owner=owner
		self.length=length
		self.width=width
		self.height=height

if __name__=='__main__':
	a=Car
	b=Car(20,22,25,'cat')
	print a.length
	#del a.owner
	print b.length
	#print a.name
