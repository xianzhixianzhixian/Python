#!/usr/bin/python
#coding=utf-8
#python操作redis数据库

import redis

redisconn=redis.Redis(host='192.168.56.101',port=6379,db=0)
redisconn.lpush('redispython','day3_first')
print(redisconn.lindex('redispython',0))
print(redisconn.llen('redispython'))
print(redisconn.lrange('redispython',0,99))
print(redisconn.lpop('redispython'))