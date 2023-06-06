if __name__ == '__main__':
    while True:
        input_value_1 = input('input a number:\n')
        input_value_2 = input('input another number:\n')
        try:
            number_1 = int(input_value_1)
            number_2 = int(input_value_2)
        except ValueError:
            print('invalid param, please input only number !!!')
        else:
            sum = number_1 + number_2
            print(input_value_1 + ' + ' + input_value_2 + ' = ' + str(sum))
        is_continue = input("continue ? y or n:\n")
        if is_continue != 'y':
            break
