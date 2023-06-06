import json


def store_user():
    user_name = input('input your name:\n')
    file_path = 'txt/user.txt'
    with open(file_path, 'w') as file_obj:
        json.dump(user_name, file_obj)
    return user_name


def get_stored_user():
    file_path = 'txt/user.txt'
    try:
        with open(file_path) as file_obj:
            user_name = json.load(file_obj)
    except FileNotFoundError:
        return store_user()
    else:
        return user_name


def greet_user():
    user_name = get_stored_user()
    print('Welcome !!! ' + user_name)


if __name__ == '__main__':
    greet_user()