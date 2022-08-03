# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    print(name + " ==== ")
    message1 = "ada vice"
    message2 = 'ad as"''"'
    print(message1.title())
    print(message2.upper())

    a = "abc\ndsa\ndas\tdasd\tds"
    print(a)

    b = "       das dsa      "
    print("b: " + b)
    print("b.trim: " + b.strip() + "|")
    print("b.ltrim: " + b.lstrip() + "|")
    print("b.rtrim: " + b.rstrip() + "|")

    print("asd'ds ")


def print_num():
    print(1)
    print(1 + 2)
    print(2 * 2)
    print(3 / 2)  # 1.5
    print(int(3 / 2))  # 1
    print(3 ** 3)

    print(0.1 + 0.2)

    print(" " + str(23))

# 1
# 3
# 4
# 1.5
# 27
# 0.30000000000000004
#  23


if __name__ == '__main__':
    print_hi("name")
    print_num()