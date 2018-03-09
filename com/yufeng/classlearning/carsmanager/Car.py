#!/usr/bin/python
#coding=utf-8
#汽车实体类
#yufeng on 2018/3/9

class Car(object):
    __id=0 #id
    __carnum=0 #车牌号
    __carname='' #车名
    __carcolor='' #车的颜色
    __status=0 #车是否空闲
    __day_pay=0 #日租价
    __is_delete=0 #是否为报废车辆

    # def __init__(self):
    #     self.__id = 0  # id
    #     self.__carnum = 0  # 车牌号
    #     self.__carname = ''  # 车名
    #     self.__carcolor = ''  # 车的颜色
    #     self.__status = ''  # 车是否空闲
    #     self.__day_pay = 0  # 日租价
    #     self.__is_delete = 0  # 是否为报废车辆

    def getId(self):
        return id

    def setId(self,id):
        self.__id=id

    def getCarnum(self):
        return self.__carnum

    def setCarnum(self, carnum):
        self.__carnum = carnum

    def getCarname(self):
        return self.__carname

    def setCarname(self, carname):
        self.__carname = carname

    def getCarcolor(self):
        return self.__carcolor

    def setCarcolor(self, carcolor):
        self.__carcolor = carcolor

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def getDaypay(self):
        return self.__day_pay

    def setDaypay(self, day_pay):
        self.__day_pay = day_pay

    def getIsDelete(self):
        return self.__is_delete

    def setIsDelete(self, is_delete):
        self.__is_delete = is_delete