if __name__ == '__main__':
    # 1. for 循环列表
    names = ['李白', 'Tom', '丽丽', 'Jim']
    for name in names:
        print(name)
    for name in names:
        print(name.title() + ", xxxx xx xxxx xx!")
        print('xxxxxxxxxxxx xxxx ,' + name + ".\n")
    # 2. for 循环需要注意缩进
    print('for end ===')
    #    print(1) 不必要的缩进会报错

    # 3.range 函数
    for i in range(1,5):
        print(i) # 左闭右开 1 2 3 4

    numbers = list(range(1, 11, 2))
    print(numbers) # 带步长

    list = []
    for i in range(1, 11):
        list.append(i ** 2)
    print(list)
    print(min(list))
    print(max(list))
    print(sum(list))

    # 4. 列表解析
    list = [i ** 3 for i in range(1, 11)]
    print(list)

    # 5. 切片
    list = [i for i in range(1, 8)]
    print(list)
    print(list[1:4])  # 左闭右开，第1到3共3个元素
    print(list[3:])
    print(list[-3:])  # 5, 6, 7

    # 6. 遍历切片列表
    # 7. 数组的复制
    list_1 = [1]
    list_1_ = list_1[:]
    list_1_.append(2)
    print(list_1)  # [1] 使用切片拷贝值

    list_2 = [1]
    list_2_ = list_2
    list_2_.append(2)
    print(list_2)  # [1, 2] 直接传值，同一对象

    #  8. 元祖（不可变的数组）
    dimension = (2, 4, 6)
    print(dimension)
    print(dimension[1])
    #  dimension[1] = 1  TypeError: 'tuple' object does not support item assignment
    print(dimension[1:])

