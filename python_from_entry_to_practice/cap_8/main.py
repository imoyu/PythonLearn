def func_1(name, age):
    print('#1 name ' + name + ', age ' + str(age))


# 参数默认值，带默认值的放后面
def func_2(name, age=3):
    print('#2 name ' + name + ', age ' + str(age))


# 可以使用 `:` 指定类型(ide类型检查，实际无约束作用)
# 类型：int(数字，包括浮点数), str, list, tuple, dict
def get_name(first_name: str, last_name: str):
    name = first_name.title() + ' ' + last_name.title()
    return name

# 接收浮点数
def print_num(num: int):
    print(num)


# 构造可选的参数
def get_name_2(first_name: str, last_name: str, middle_name=''):
    if middle_name == '':
        name = first_name.title() + ' ' + last_name.title()
    else:
        name = first_name.title() + ' ' + middle_name.title() + ' ' + last_name.title()
    return name


# 返回字典
def build_person(first_name: str, last_name: str):
    person = {
        'first': first_name,
        'last': last_name
    }
    return person


# 返回字典
def build_person_2(first_name: str, last_name: str, age=''):
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age
    return person


# 传递列表
def print_list(names):
    for name in names:
        print(name)


# 改变是永久的
def add_x_to_list_1(chars:list):
    chars.append('x')


# 不改变的方法
# def add_x_to_list_2(chars[:]): # ?? 无效
#     chars.append('x')


# 传递若干参数
# * 表明 params 是一个 tuple，存放输入的值
def print_tuple_params(*params):
    print(params)


# 传递若干 dict 参数
# ** 表明 params 是一个 dict，存放输入的 k-v 值
def print_dict_params(name, **params):
    print(name + ": " + str(params))


#  模块，见 P133


if __name__ == '__main__':
    # 位置实参
    func_1('xiaoming', 12)
    # 关键字实参
    func_1(name='mx', age=33)
    func_1(age=33, name='fs')
    # func_1(name='xiaoming', 12) # 使用关键字后，剩余参数都要使用关键字参数
    # func_1('xiaoming', age = 12) # 这样的可以

    func_2('coco')
    print(get_name('michael', 'jackson'))
    print(2.33)

    print(get_name_2('san', 'do'))
    print(get_name_2('san', 'do', 'nana'))

    print(build_person('coco', 'dai'))
    print(build_person_2('coco', 'dai'))
    print(build_person_2('cocox', 'daix', 23))

    print_list(['sd', 'vc', 'gf', 'po'])

    list = []
    add_x_to_list_1(list)
    print(list)

    print_tuple_params('das', 'cx', 'ytd')
    print_dict_params('dict_param', age=12, color='yellow')