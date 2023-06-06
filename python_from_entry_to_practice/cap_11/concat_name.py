def get_name(first_name: str, last_name: str):
    return first_name.title() + ' ' + last_name.title()

# py 中方法不能重载，后面的同名方法会覆盖前面的
def get_name_2(first_name: str, last_name: str, mid_name):
    return first_name.title() + ' ' + last_name.title() + ' ' + mid_name