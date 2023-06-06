# 8.3
def shirt(size, word):
    print('size is ' + size + ', word is' + word)


def print_animals(animals):
    print(animals)
    animals.append('xxx')


if __name__ == '__main__':
    shirt('XXL', 'word peace 1')
    shirt(word='word peace 2', size='XXL')
    # 默认值
    shirt('XXL', word='word peace 3')

    animals = ['a', 'b', 'c']
    animals_2 = animals[:]
    print_animals(animals)
    print(animals)

    print_animals(animals_2[:])
    print(animals_2)

