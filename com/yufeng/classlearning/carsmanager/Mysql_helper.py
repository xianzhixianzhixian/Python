#!/usr/bin/python
#coding=utf-8
#使用python操作mysql数据库工具类
#yufeng on 2018/3/9

import pymysql
from com.yufeng.classlearning.carsmanager.Car import Car

class Mysql_helper(object):
    #包括数据库的增删改
    @staticmethod
    def update(sql):
        # 连接数据库
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='cars', charset='utf8')
        statement = conn.cursor()
        # 查询
        try:
            num = statement.execute(sql)
            conn.commit()
            return num
        except Exception as e:
            conn.rollback()
            print("Exception", e)
        finally:
            statement.close()
            conn.close()

    #包括数据库的查询
    @staticmethod
    def selectAllCar():
        # 连接数据库
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='cars', charset='utf8')
        statement = conn.cursor()
        # 查询
        sql='select * from cars where is_delete=0'
        try:
            statement.execute(sql)
            results = statement.fetchall()
            list = []
            for row in results:
                car = Car()
                id = row[0]
                carnum = row[1]
                carname = row[2]
                carcolor = row[3]
                status = row[4]
                daypay = row[5]
                is_delete = row[6]
                car.setId(id)
                car.setCarnum(carnum)
                car.setCarname(carname)
                car.setCarcolor(carcolor)
                car.setStatus(status)
                car.setDaypay(daypay)
                car.setIsDelete(is_delete)
                list.append(car)
            return list
        except Exception as e:
            print("Exception", e)
        finally:
            statement.close()
            conn.close()