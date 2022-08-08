from collections import OrderedDict as od

# 引入标准库
if __name__ == '__main__':
    favorite_language = od()

    favorite_language['Jerry'] = 'C'
    favorite_language['Tom'] = 'Java'
    favorite_language['Jimmy'] = 'Go'

    for name, language in favorite_language.items():
        print(name + ' likes ' + language + ' most')