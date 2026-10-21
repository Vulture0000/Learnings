class Animal:
    def __init__(self):#`__init__` is basically like a constructor, but in Python, it only assigns the values. What does that mean? It only assigns the value to the object, but it doesn't create the object. To create an object, we need to call the inbuilt function, which is `__new__`. The `init` only initializes the object, not creating 
        pass
    #Basically, the `self` keyword is like the `this` keyword in Java, which will only point out what the object we are currently working on is. The current state will be, or the current value will be, Vincent itself, like the `this` keyword in Java. 
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
