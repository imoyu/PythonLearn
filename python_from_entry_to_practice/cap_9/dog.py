class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " sit")

    def roll_over(self):
        print(self.name + " rolled over")


if __name__ == '__main__':
    dog = Dog('wilson', 12)
    print(dog.name)
    print(dog.age)
    dog.sit()
    dog.roll_over()