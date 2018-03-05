#!/usr/bin/python
#coding=utf-8
#Filename:while.py
from pip._vendor.distlib.compat import raw_input

number=23
running=True

while running:
	guess=int(raw_input("Enter an integer:"))
	
	if guess==number:
		print ("Congratulations, you guessed it.")
		running = False # this causes the while loop to stop
	elif guess<number:
		print ("No, it is a little higher than that")
	else:
		print ("No, it is a little lower than that")
else: #这里的else表示下面的print语句是while循环之外的,如果去除了这里的else,下面的print语句就属于循环内的else了
	print ("The while loop is over.")
	# Do anything else you want to do here
print ("Done")
