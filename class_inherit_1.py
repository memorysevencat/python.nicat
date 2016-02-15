#!/usr/bin/python2
#coding:utf-8
#copyright by sevencat

class Employee(object):
	def __init__(self,name,job=None,pay=0):
		self._name=name
		self._job=job
		self._pay=pay
	def giveRaise(self,percent):
		self._pay=int(self._pay*(1+percent))
	def __str__(self):
		return '[Employee:%s,%s,%s]'%(self._name,self._job,self._pay)

class Manager(Employee):
	def __init__(self,name,pay):
		Employee.__init__(self,name,'mgr',pay)
	def giveRaise(self,percent,bonus=.10):
		Employee.giveRaise(self,percent+bonus)

if __name__=='__main__':
	a=Employee("xiaoli",'engineer1',10000)
	b=Employee("xiaowang",'engineer2',20000)
	c=Manager("xiaozhang",30000)
	members=[a,b,c]
	for member in members:
		member.giveRaise(0.1)
		print member
