if __name__ == '__main__':
    # 读取全部内容
    with open('txt/pi_digits.txt') as file_obj:
        # read 方法会返回一个换行符
        contents = file_obj.read()
        print(contents.rstrip())

    # 逐行读取 末尾带一个换行符，print 也带一个
    with open('txt/pi_digits.txt') as file_obj:
        for line in file_obj:
            print(line.rstrip())

    # 全局使用文件内容
    with open('txt/pi_digits.txt') as file_obj:
        lines = file_obj.readlines()
    print(lines)

    # 分析生日是否在圆周率中
    birthday = '1212'
    with open('txt/pi_million_digits.txt') as file_obj:
        result = ''
        for line in file_obj:
            result += line.rstrip()
    if birthday in result:
        print('yes ~~~')

    # 写入文件
    # 无文件时自动创建
    file_name = 'txt/programing.txt'
    with open(file_name, 'w') as file_obj:
        file_obj.write('I am running ...')

    # 附加写
    with open(file_name, 'a') as file_obj:
        for index in range(10):
            file_obj.write('\nLine ' + str(index + 1) + ' ======= ')

    # 异常的处理
    # else 仅当未发生异常时调用
    try:
        print('exec try ...')
        result = 5 / 0
        print('exec after exception')
    except ZeroDivisionError:
        print("can't divide by 0 !!!")
    else:
        print(result)

    try:
        with open('txt/null.txt') as file_obj:
            print(file_obj.readlines())
    except FileNotFoundError:
        print('file not exist ...')

    # 分析单词数量
    book_name = 'alice.txt'
    try:
        with open('txt/' + book_name) as file_obj:
            contents = file_obj.read()
        words = contents.split()
        print(book_name + ' has ' + str(len(words)) + ' words')
    except FileNotFoundError:
        print('file not exist ...')

    # pass 跳过异常处理
    try:
        print('before ...')
        result = 3 / 0
        print('after ...')
    except ZeroDivisionError:
        pass
