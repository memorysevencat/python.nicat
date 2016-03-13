#!/usr/bin/python2
#coding:utf-8
#copyright by sevencat
class RegisterClass(type):
	def __init__(cls, name, bases,nmspc):
		super(RegisterClass, cls).__init__(name, bases,nmspc)
		if not hasattr(cls,'registry'):
			cls.registry=set()
		cls.registry.add(cls)
		cls.registry-=set(bases)
	def __iter__(cls):
		return iter(cls.registry)
	def __str__(cls):
		if cls in cls.registry:
			return cls.__name__
		return cls.__name__+":"+",".join([sc.__name__ for sc in cls])

Shape=RegisterClass('Shape',(),{})
class Round(Shape):pass
class Square(Shape):pass
class Triangular(Shape):pass
class Boxy(Shape):pass
print Shape
class Circle(Round):pass
class Ellipse(Round):pass
print Shape

for s in Shape:
	print s
print '###'
print Round.registry==Shape.registry
a=Round()
print a.registry==Shape.registry
