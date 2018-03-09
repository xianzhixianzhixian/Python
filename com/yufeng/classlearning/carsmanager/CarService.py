#!/usr/bin/python
#encoding=utf-8
#Car操作的service
#yufeng on 2018/3/9

from com.yufeng.classlearning.carsmanager.Mysql_helper import Mysql_helper
from com.yufeng.classlearning.carsmanager.Car import Car

class CarService(object):

    #添加汽车
    def addCar(self):
        car=Car()
        car.setCarnum(input('请输入车牌号：'))
        car.setCarname(input('请输入车名：'))
        car.setCarcolor(input('请输入颜色：'))
        car.setDaypay(input('请输入日租价：'))

        sql='insert into cars(carnum,carname,carcolor,daypay)values(%s,%s,%s,%s)' %(car.getCarnum(),car.getCarname(),car.getCarcolor(),car.getDaypay())
        return Mysql_helper.update(sql)

    #租车
    def rentCar(self):
        CarService.showAllCar()
        carnum=input('请输入你选择的车牌：')
        sql = 'update cars set status=%d where carnum=%s and is_delete=%d' %(1,carnum,0)
        return Mysql_helper.update(sql)

    # 还车
    def giveBackCar(self):
        CarService.showAllCar()
        carnum = input('请输入你选择的车牌：')
        sql = 'update cars set status=%d where carnum=%s and status=%d and is_delete=%d' %(0,carnum,1,0)
        return Mysql_helper.update(sql)

    # 报废汽车
    def deleteCar(self):
        CarService.showAllCar()
        carnum = input('请输入你选择的车牌：')
        sql = 'update cars set is_delete=%d where carnum=%s and is_delete=%d' %(1,carnum,0)
        return Mysql_helper.update(sql)

    @staticmethod
    def showAllCar():
        list=Mysql_helper.selectAllCar()
        print('车牌号\t车名\t颜色\t在库状态\t日租金')
        for car in list :
            statestr = '使用中'
            if car.getStatus()==0:
                statestr = "空闲"
            resultstr= "%s\t%s\t%s\t%s\t%s" % (str(car.getCarnum()),str(car.getCarname()),str(car.getCarcolor()),statestr,str(car.getDaypay()))
            print(resultstr)