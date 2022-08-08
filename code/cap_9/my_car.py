from car import Car

# 导入类
car_1 = Car('audi', 'a4', 2019)
print(car_1)
print(car_1.get_description())

'''
一个模块中可以定义多个类
可以从一个模块中导入多个类
可以导入整个模块：import car
    调用的时候，需要指明模块：car.Car(xxx, xxx, xxx)
'''