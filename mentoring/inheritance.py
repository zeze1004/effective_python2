from typing import List

class Animal:
    def bark(self):
        print("???")

class Dog(Animal):
    def bark(self):
        print("멍멍")

class Duck(Animal):
    def bark(self):
        print("꿱꿱")


animals: List[Animal] = []
animals.append(Duck())
animals.append(Dog())

for animal in animals:
    animal.bark()


Functional Language <-> Object-oriented Language
