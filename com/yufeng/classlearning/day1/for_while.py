#!/usr/bin/python
#coding=utf-8
#for while循环的使用
sum=0.0
list_example=['a','b','c','d','e','f']
for l in list_example:
    print('element：',l)

while sum<100:
    sum+=0.5
    print("sum：",sum)

print("所有循环结束")