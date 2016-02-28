class Foo(object):
	pass

def howdy(self,you):
	print "howdy,",you

class Event(object):
	events=[]
	def __init__(self, action, time):
		self.action=action
		self.time=time
		Event.events.append(self)

	def __cmp__(self,other):
		return cmp(self.time,other.time)

	def run(self):
		print "%.2f : %s" % (self.time,self.action)
	@staticmethod
	def run_events():
		Event.events.sort();
		for e in Event.events:
			e.run()
def create_mc(description):
	class_name="".join(x.capitalize() for x in description.split())
	def  __init__(self, time):
		Event.__init__(self,description+"  [mc]",time)
	globals()[class_name]=type(class_name,(Event,),dict(__init__=__init__))

def create_exec(description):
	class_name="".join(x.capitalize() for x in description.split())
	klass="""
class %s(Event):
	def __init__(self,time):
		Event.__init__(self,"%s [exec]",time)
""" % (class_name,description)
	exec klass in globals()
if __name__=='__main__':
	Foo.a=42
	x=Foo()
	print x.a
	Foo.method=lambda self:"hi"
	print x.method()
	F=type('Foo',(),{})
	print F
	print '########'

	M=type('a',(list,),dict(x=42,howdy=howdy))
	ml=M()
	ml.append("007")
	print ml
	print ml.x
	ml.howdy('seven cat')
	print '########'
	descriptions = ["Light on", "Light off", "Water on", "Water off","Thermostat night", "Thermostat day", "Ring bell"]
	initializations = "ThermostatNight(5.00); LightOff(2.00); WaterOn(3.30); WaterOff(4.45); LightOn(1.00); RingBell(7.00); ThermostatDay(6.00)"
	[create_mc(dsc) for dsc in descriptions]
	exec initializations in globals()
	[create_exec(dsc) for dsc in descriptions]
	exec initializations in globals()
	Event.run_events()
