class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        long_name = self.make + ' ' + self.model + ' ' + str(self.year)
        return long_name.title()

    def update_year(self, year: int):
        if year < 0:
            print('year is invalid ...')
        else:
            self.year = year


if __name__ == '__main__':
    new_car = Car('audi', 'a4', 2019)
    print(new_car.get_description())
    # 修改属性
    new_car.year = 2020
    # 通过方法修改
    new_car.update_year(2011)
    print(new_car.year)

