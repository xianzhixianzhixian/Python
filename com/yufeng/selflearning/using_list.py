#!/usr/bin/python
#Filename:using_list.py

#This is my shoppinglist
shopList=['apple','mango','carrot','banana'] #like array

print ('I hava ',len(shopList),' items to our purchase.')

print ('These items are:\n'),#Notice the comma at end of the line
for item in shopList:
	print (item),# , is not necessary
print ('\n I also have to buy rice.')
shopList.append('rice')
print ('My shopping list is now',shopList)

print ('I will sort my list now')
shopList.sort()
print ('Sort shopping list is ',shopList)

print ('The first item I will buy is ',shopList[0])
olditem=shopList[0]
del shopList[0]
print ('I bought the',olditem)
print ('My shopping list is now ',shopList)

