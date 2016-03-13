#!/usr/bin/python2
#coding:utf-8
#copyright by sevencat

class A:
	def test(self):
		print 'A test'

class B(A):
	def test(self):
		print 'B test'
		A.test(self)
class C(A):
	def test(self):
		print 'C test'
		A.test(self)
class D(B,C):
	def test(self):
		print "D test"
		B.test(self)
		C.test(self)
class AA(object):
	def test(self):
		print 'AA test'
class BB(AA):
	def test(self):
		print 'BB test'
		super(BB,self).test()
class CC(AA):
	def test(self):
		print 'CC test'
		super(CC,self).test()
class DD(BB,CC):
	def test(self):
		print "DD test"
		super(DD,self).test()

if __name__=="__main__":
	a=D()
	a.test()
	print '-----'
	a=DD()
	a.test()
