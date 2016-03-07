#!/usr/bin/python2
#coding:utf-8
#copyright by sevencat
class base_class(object):
	events=[]
	def __init__(self, members):
		self.members=members	
		base_class.events.append(self)
	def run(self):
		print self.members
	@staticmethod
	def run_event():
		for e in base_class.events:
			e.run()

def create_class(description):
	def __init__(self, members):
		base_class.__init__(self,description+" "+members)
	class_name="".join(x.capitalize() for  x in description.split())
	print class_name
	globals()[class_name]=type(class_name,(base_class,),dict(__init__=__init__))

if __name__=='__main__':
	descriptions=["class_one","class_two","class_three"]
	[create_class(dsc) for dsc in descriptions]
	initializatons = "Class_one('5')"
	exec initializatons in globals()
	base_class.run_event()

