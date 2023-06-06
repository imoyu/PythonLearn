import json

if __name__ == '__main__':
    try:
        with open('../txt/favorite_number.txt') as file_obj:
            # 返回值和 json 内容相关
            number = json.load(file_obj)
    except FileNotFoundError:
        number = input("what's your favorite number ?\n")
        with open('../txt/favorite_number.txt', 'w') as file_obj:
            json.dump(number, file_obj)
    print('Your favorite number is ' + str(number))