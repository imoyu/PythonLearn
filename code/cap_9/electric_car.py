from cap_9.car import Car


# 继承类
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 调用父类构造器
        super().__init__(make, model, year)
        # 自己的属性
        self.code = 'ak4787623'

    # 重写方法
    def get_description(self):
        long_name = "ECar " + self.make + ' ' + self.model + ' ' + str(self.year)
        return long_name.title()


if __name__ == '__main__':
    e_car = ElectricCar('toyuta', 'a9', 2015)
    print((e_car.get_description()))
    print(e_car.code)
    print(e_car.model)