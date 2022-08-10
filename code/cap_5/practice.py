# 5.3
def get_stage(age:int):
    if age < 2:
        print('婴儿')
    elif age <= 4:
        print('学步')
    elif age <= 13:
        print('儿童')
    elif age <= 20:
        print('青少年')
    elif age <= 65:
        print('成年')
    else:
        print('老年')


# 5.8~10
def users_check(users):
    for user in users:
        if user == '':
            print('Empty User')
        elif user == 'admin':
            print('Hello admin')
        else:
            print('user: ' + user)

    new_users = ['aa', 'bb', 'cc', 'dd']
    for new_user in new_users:
        if new_user in users:
            print(new_user + ' is used')
        else:
            print(new_user + "is not used")


if __name__ == '__main__':
    # 5.2
    print('DS' == 'ds')
    print('DS'.lower() == 'ds')
    print(12 == 13)
    print(12 != 13)
    print(12 > 13)
    print(12 < 13)
    print(True or False)
    print(True or False and False)

    get_stage(65)
    get_stage(35)
    get_stage(2)

    users = ['cc', 'bb', '', 'das', 'okw', 'pdo']
    users_check(users)