if __name__ == '__main__':
    question = input('input your question:')
    print(question
          .replace('are you', '')
          .replace('?', '.'))

    # int() 转换输入的字符串
    num = int(input('input a number :\n'))
    print(num)

    # 取模
    print(103 % 7)

    # while 循环
    index = 1
    while index <= 5:
        print('index: ' + str(index))
        index += 1

    # input + while
    message = ''
    res = ''
    while message != 'end':
        message = input('input your message:')
        if message == 'end':
            continue
        res += message + '\n'
    print('your total input is :\n' + res)

    # break 和 continue 略

    # while 循环列表
    users = ['aa', 'vv', 'kk', 'pp']
    while users:
        users_pop = users.pop()
        print(users_pop)
    print('end users pop')

    # 可以删除，但是会导致 index 匹配不上
    # users = ['aa', 'vv', 'kk', 'pp']
    # for index in range(0, len(users)):
    #     print(users[index])
    #     del users[index]

    # 删除 list 中特定元素
    list = ['asd', 'fd', 'fd', 'dfx', 'dsy', 'gfd', 'ouy']
    print(list)
    while 'fd' in list:
        list.remove('fd')
    print(list)

