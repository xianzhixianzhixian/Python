#!/usr/bin/python
#coding=utf-8
#Filename=utf-8
from pip._vendor.distlib.compat import raw_input

while True:
	s=raw_input("Enter something:")
	if s=="quit":
		break
	if(len(s)<3):
		continue
print ("Input is of sufficience length")
#Do other kinds of processing here
