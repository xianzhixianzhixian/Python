#!/usr/bin/python
#coding=utf-8
#Filename:break.py
from pip._vendor.distlib.compat import raw_input

while True:
	s=raw_input("Enter somthing:")
	if s=="quit":
		break
	print ("Length of the string is",len(s))
print ("Done")
