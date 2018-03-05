#!/usr/bin/python
#Filename:func_globalvariable.py

def func():
	global x #golbal is used to change value of variable outside the function
	print ('x is',x)
	x=2
	print ('Change local x to ',x)

x=50
func()
print ('Value of x is ',x)
