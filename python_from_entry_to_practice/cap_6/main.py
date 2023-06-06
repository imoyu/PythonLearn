def dictionary():
    alien = {'color': 'green', 'point': 5}
    # 1. 查询
    print(alien['point'])
    # print(alien['x'])  KeyError
    # 2. 添加
    print(alien)
    alien['name'] = 'cake'
    print(alien)
    # 3. 修改
    # 4. 删除
    del alien['name']
    print(alien)
    # 5. 空字典
    empty_dictionary = {}


def traversal():
    country = {
        'libai': 'England',
        'wangwang': 'China',
        'kangkang': 'China',
        'yuki': 'Japan',
        'lucy': 'Canada',
        # 'lucy': 'Canada1' 出现重复key，覆盖之前的
    }
    # 遍历字典
    for key, value in country.items():
        print("name: " + key + "  " + "country: " + value)
    for key in country.keys():
        print(key)
    for value in country.values():
        print(value)

    # 按照 key 排序输出
    for key in sorted(country.keys()):
        print(key + ':' + country[key])

    # set
    country_set = set(country.values())
    for value in country_set:
        print(value)

    # 嵌套
    # 1. 列表嵌套字典
    aliens = []
    for index in range(1, 31):
        new_alien = {'color': 'green', 'point': 10, 'name': 'alien_' + str(index)} #  index 是 int，不能直接与str相加
        aliens.append(new_alien)
    for alien in aliens:
        print(alien)
    print('name of alien 5: ' + aliens[4]['name'])
    # 2. 字典嵌套列表
    map = {
        'l1': ['cc1', 'aa1', 'bb1'],
        'l2': ['cc2', 'aa2', 'bb2'],
        'l3': ['cc3', 'aa3', 'bb3']
    }
    print(map['l2'][2])
    # 3. 字典嵌套字典
    map = {
        'm1': {'x': 12, 'y': 99},
        'm2': {'x': 15, 'y': 88},
    }
    print(map['m2']['y'])

if __name__ == '__main__':
    dictionary()
    traversal()