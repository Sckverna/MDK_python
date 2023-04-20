from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass
class Cat(Animal):
    def say(self):
        print("Meow!")

class Dog(Animal):
    def say(self):
        print("Woof!")

dog = Dog("red","sharik",7)
cat = Cat("green","lol",5)
cat.say()
dog.say()