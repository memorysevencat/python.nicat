#!/usr/bin/python2
#coding:utf-8
#copyright by sevencat

class Date(object):
	def __init__(self,day=0,month=0,year=0):
		self.day=day
		self.month=month
		self.year=year

	def __str__(self):
		return "{0}-{1}-{2}".format(self.year,self.month,self.day)

	@classmethod
	def from_string(cls,date_as_string):
		year,month,day=map(int,date_as_string.split('-'))
		date1=cls(day,month,year)
		return date1

	@staticmethod
	def is_date_valid(date_as_string):
		year,month,day=map(int,date_as_string.split('-'))
		return day <= 31 and month<= 12 and year <=3999

	@staticmethod
	def millenium(month,day):
		return Date(month,day,2016)

class DateTime(Date):
	def __str__(self):
		return "{0}-{1}-{2}-00:00:00".format(self.year,self.month,self.day)

if __name__=='__main__':
	s='2016-02-13'
	if Date.is_date_valid(s):
		date1=Date.from_string(s)
		print date1
		date2=DateTime.from_string(s)
		print date2

	millenium1=Date.millenium(1,2)
	print millenium1
	millenium2=Date.millenium(3,4)
	print millenium2
