from os import name


class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"{self.name} is a {self.breed}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def details(self):
        print(f"{self.name} is a {self.breed}.")

w = Dog("Buddy", "Golden Retriever")

w.info()
w.details()