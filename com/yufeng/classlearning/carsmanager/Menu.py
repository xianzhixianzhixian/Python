#!/usr/bin/python
#coding=utf-8
#汽车管理界面菜单
#yufeng on 2018/3/9

from com.yufeng.classlearning.carsmanager.CarService import CarService

def menu():
    print('    【汽车租赁系统】')
    print('---------------------------------')
    print('    1.汽车信息添加')
    print('    2.汽车信息浏览')
    print('    3.租车')
    print('    4.还车')
    print('    5.报废汽车')
    print('    0.退出')
    print('---------------------------------')
    print(' ')
    carservice=CarService()
    selection = input('输入选项：')
    print(selection)
    if selection==0:
        exit(0)
    elif selection=='1':
        if carservice.addCar()>=1:
            print('添加汽车成功')
        else:
            print('添加汽车未成功')
    elif selection == '2':
        carservice.showAllCar()
    elif selection == '3':
        if carservice.rentCar()>=1:
            print('租赁汽车成功')
        else:
            print('租赁汽车未成功')
    elif selection == '4':
        if carservice.giveBackCar()>=1:
            print('归还汽车成功')
        else:
            print('归还汽车未成功')
    elif selection == '5':
        if carservice.deleteCar()>=1:
            print('报废汽车成功')
        else:
            print('报废汽车未成功')
    else:
        print('输入选项错误')

if __name__ == "__main__":
    while True:
        menu()