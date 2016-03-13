globals={'x':7,'y':10,'core':[10,11,12]}
locals={'x':1,'y':10,'core':[10,15,12]}
a=eval('3*x+4*y',globals,locals)
print a
str='print 1+2'
exec 'for b in core:print b' in globals,locals
exec compile(str,'','exec') 
