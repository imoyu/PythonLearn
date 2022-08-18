if __name__ == '__main__':
    with open('../txt/practice_1.txt', 'w') as file_obj:
        file_obj.write('What are you doing ? 1\n')
        file_obj.write('What are you doing ? 2')

    with open('../txt/practice_1.txt') as file_obj:
        contents = file_obj.read()
    print(contents)

    with open('../txt/practice_1.txt') as file_obj:
        for line in file_obj:
            print(line)

    with open('../txt/practice_1.txt') as file_obj:
        lines = file_obj.readlines()
    print(lines)
