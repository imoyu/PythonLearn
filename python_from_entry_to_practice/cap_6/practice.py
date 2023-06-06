if __name__ == '__main__':
    # 6.1
    people = {
        'name': 'nancy',
        'age': 23,
        'city': 'London'
    }
    print(people)

    # 6.6
    is_invited_dict = {
        'aa': True,
        'bb': False,
        'cc': True,
        'dd': False,
        'ee': True
    }
    for name, is_invited in is_invited_dict.items():
        if is_invited:
            print(name + ' has been Invited')
        else:
            print(name + " hasn't been Invited")
