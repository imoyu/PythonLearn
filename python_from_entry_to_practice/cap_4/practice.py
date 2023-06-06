def pizza():
    list = ['pizza1', 'pizza2', 'pizza3']
    for pizza in list:
        print('I like ' + pizza)
    print(" ============ ")


def print_from_1_to_20():
    for num in range(1, 21):
        print(num)


def print_list_1000000():
    list = [i for i in range(1, 1000001)]
    print(list)
    res = sum(list)
    print(res)


def print_odd_in_20():
    for num in range(1, 21, 2):
        print(num)


def print_list_3_in_30():
    list = [num for num in range(1, 31)]
    print(list)


def print_third_power_in_10():
    for num in range(1, 11):
        print(num ** 3)


def print_part_of_list(list):
    if len(list) < 3:
        print("长度小于3")
        return
    print('前面3个元素：' + str(list[:3]))
    start = int(len(list) / 2) - 1
    print('中间3个元素：' + str(list[start:start + 3]))
    print('后面3个元素：' + str(list[-3:]))


def pizza_2():
    list = ['pizza1', 'pizza2', 'pizza3']
    list_copy = list[:]
    list_copy.append('pizza_copy')
    list.append('pizza4')
    for pizza_copy in list_copy:
        print(pizza_copy)

def for_for():
     list1 = [1, 2, 3]
     list2 = [4, 5, 6]
     list3 = [7, 8, 9]
     lists = [list1, list2, list3]
     for list in lists:
         for num in list:
             print(num)


def menu():
    menu = ('m1', 'm2', 'm3')
    print(menu)
    # menu[1] = 'xx' #  无法修改
    menu = ('x1', 'x2', 'x3')
    print(menu)

if __name__ == '__main__':
    # 4-1
    pizza()

    # 4-3
    print_from_1_to_20()
    # 4-4,5
    print_list_1000000()
    # 4-6
    print_odd_in_20()
    # 4-7
    print_list_3_in_30()
    # 4-8
    print_third_power_in_10()

    # 4-10
    print_part_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # 4-11
    pizza_2()
    # 4-12
    for_for()

    # 4-13
    menu()
