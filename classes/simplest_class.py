class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is {}.".format(self.name))

p1 = Person('Maninder Singh')
p1.say_hi()

p2 = Person('Navjot Singh')
p2.say_hi()