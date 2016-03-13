#!/usr/bin/python2
# coding: utf-8

class SimpleMeta1(type):
    def __init__(cls, name, bases, atts):
        super(SimpleMeta1, cls).__init__(name, bases, atts)
        cls.test = lambda self : "Yes! This is a test."
        cls.att=1


class A(object):
    __metaclass__=SimpleMeta1
    
if __name__ == "__main__":
    a=A()
    print a.att,a.test()
    A=SimpleMeta1('sm',(),{})
    a=A()
    print a.att,a.test()
