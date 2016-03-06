#!/usr/bin/python2
#coding by utf-8
#copyright by sevencat
def test_fun(arg):
	x=1
	return locals()
class Event(object):
	member_one=[]
	member_two=[]
	events=[]
	def __init__(self, action, time):
		Event.member_one.append(action)
		Event.member_two.append(time)
		self.action=action
		self.time=time
		Event.events.append(self)
	def __cmp__(self,other):
		return cmp(self.time,other.time)
	def run(self):
		print "%.2f:%s" % (self.time,self.action)
	@staticmethod
	def run_events():
		Event.events.sort();
		for e in Event.events:
			e.run()

def create_mc(description):
	print '_',description
	class_name="".join(x.capitalize() for x in description.split())
	print class_name
	def __init__(self, time):
		Event. __init__(self, description+" [mc]",time)
	globals()[class_name]=type(class_name,(Event,),dict(__init__=__init__))

if __name__=='__main__':
	print test_fun(10)['arg']
	globals()["a"]=type("OBJ",(list,),dict(a=7))
	#exec  "OBJ.a" in globals()
	print globals()
	descriptions = ["Light on", "Light off", "Water on", "Water off",
                    "Thermostat night", "Thermostat day", "Ring bell"]
        initializatons = "ThermostatNight(5.00); LightOff(2.00); \
        WaterOn(3.30); WaterOff(4.45); LightOn(1.00); \
        RingBell(7.00); ThermostatDay(6.00)"
	for description in descriptions:
		class_name="".join(x.capitalize() for x in description.split())
		##print class_name
	print '######'
	[create_mc(dsc) for dsc in descriptions]
	exec initializatons in globals()
	Event.run_events()
	print dir(WaterOn)
	print ThermostatDay.member_onebbbb
	print LightOn.member_two
