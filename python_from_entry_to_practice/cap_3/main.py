def test_list():
    names = ['das', '李白', '王明']
    print(names)
    print(names[0])
    print(names[1])
    print(names[2])

    # 返回最后一个元素 -2， -3 类似，从后开始索引
    print(names[-1])

    # 测试：list 中的值是否引用
    names_1 = names[1]
    names_1 = 'xx'
    print(names)  # ['das', '李白', '王明']

    # 修改元素
    names[1] = 'xx'
    print(names)

    # 添加元素
    names.append(1)
    names.insert(0, 2)
    print(names)  # [2, 'das', 'xx', '王明', 1]

    # 删除元素 3种方式
    del names[2]
    names_pop = names.pop()  # 默认 -1 位置
    names_pop = names.pop(0)
    print(names)
    names.remove('王明')  # 移除第一个改元素，找不到报错

    # 排序
    names.sort()
    names.sort(reverse=True)

    sorted(names)  # 临时排序

    # 翻转
    nums = [1, 2, 5, 8]
    reverse = nums.reverse()
    print(nums)
    print(reverse)  # None : 方法无返回值

    # 长度
    print(len(nums))

if __name__ == '__main__':
    test_list()
