class Animal:
    def __init__(self):#
        pass
    def walk(self):
        return "All animal walks"
    def sound(self):
        return "there will be different sound for each animal"
class Dog(Animal):
    def walk(self):
        return "Dog walks"
    def sound(self):
        return "bark"


animal1 = Animal()
print(animal1.walk())
print(animal1.sound())

animal2 = Dog()
print(animal2.walk())
print(animal2.sound())
