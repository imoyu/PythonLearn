def print_car():
    cars = ['audi', 'bmw', 'toyota', 'bench']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())


def compare():
    # == 比较字符串，数字
    letter = 'abc'
    print('abc' == letter)
    print(123 == (100 + 23))
    #  多条件比较
    print('a' == 'a' and 'b' == 1)
    print('a' == 'a' or 'b' == 1)


def if_elif_else():
    # input 得到的是字符串
    score = int(input())
    if score < 60:
        print('不及格')
    elif score < 80:
        print('及格')
    elif score < 90:
        print('良好')
    else:
        print('优秀')


def empty_list():
    print("======== empty_list")
    names = []
    print(names)
    for name in names:
        print(name)
    if not names:
        print("names is empty")
    names.append("xiaoHong")
    if names:
        print("name is not empty")
    #  判断列表为空的3种方法
    #  1. if list == []
    #  2. if len(list) == 0
    #  3. if not list:



def list_contains():
    dict = ['d', 's', 'z', 'j']
    print('f' in dict)
    print('z' in dict)
    if 's' in dict:
        print(3123)


if __name__ == '__main__':
    print_car()
    compare()
    if_elif_else()
    empty_list()
    list_contains()