#!/usr/bin/python
#coding=utf-8
#Filename:using_tuple.py
#list和tuple非常相似，但是tuple一旦初始化便不能改变

zoo=('wolf','elephant','penguin') #like ArrayList,Vector

new_zoo=('monkey','dolphin',zoo)
print ('Number of animals in the new zoo is ',len(new_zoo))
print ('All animals in new zoo are ',new_zoo)
print ('Animals brought from old zoo are ',zoo)
print ('Last animal brought from old zoo is ',new_zoo[2][2])