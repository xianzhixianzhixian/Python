#!/usr/bin/python
#Filename if.py
from pip._vendor.distlib.compat import raw_input

number=23
guess=int(raw_input("Enter one integer:"))

if guess==number:
	print ("Congretulations,you guessed it.") #New block starts here
	print ("(but you do not win any prizes!)" )#New blocks ends here
elif guess<number:
	print ("No,it is a little higher than that") #Another bolck
	#You can do whatever you want in a block..........
else:
	print ("No,it is a little lower than that")
print ("Done")
#This last statement is always executed, after the if statement is executed
