# pascal programming language

class Point:

    def __init__(self, x, y):
        # called when you create a new instance
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()

# point1.move()
# point1.draw()
# point1.x = 10
# point1.y = 20

# print(point1.x)
# print(point1.y)


class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John")
john.talk()


class Mammal:

    def walk(self):
        print("walk")


class Dog(Mammal):

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"Woof! My name is {self.name}")


class Cat(Mammal):

    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"Meow! My name is {self.name}")


dog1 = Dog("Fido")
dog1.bark()
