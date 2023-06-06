if __name__ == '__main__':
    # 7.2
    guess_num = int(input('多少人用餐？\n'))
    if guess_num > 8:
        print('无座位')
    else:
        print('有座位')