#!/usr/bin/python2
#coding:utf-8
#copyright by sevencat

class Employee(object):
	def __init__(self,name,job=None,pay=0):
		self._name=name
		self._job=job
		self._pay=pay
	def giveRaise(self,percent):
		self._pay=int(self._pay*(1+percent))
	def __str__(self):
		return '[Employee: %s,%s,%s]' % (self._name,self._job,self._pay)

class Manager(Employee):
	def __init__(self,name,pay):
		super(Manager,self).__init__(name, 'mgr', pay)
	def __init__(self, percent, bonus=0.10):
		super(Manager, self).__init__(percent+bonus)

class Department(object):
	def __init__(self, *args):
		self.members=list(args)
	def  addMemver(self,person):
		self.members.append(person)
	def showAll(self):
		for person in self.members:
			print person
	def giveRaise(self,percent):
		for person in self.members:
			person.giveRaise(percent)

if __name__=='__main__':
	a=Employee("xiaoone",'engineer_one',10000)
	b=Employee("xiaotwo",'engineer_two',12000)
	c=Employee("xiaothree",'engineer_three',13000)

	d=Department(a,b,c)
	d.showAll()
	d.giveRaise(0.5)
	d.showAll()
