# init is automatically called sort of like a constructor in JavaScript
# self is like this in JavaScript

class Puppy:
    def __init__(self, name):
        self.name = name
        self.tricks = []


puppy_obj = Puppy("Name")
print(puppy_obj.name)
print(puppy_obj.tricks)


class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
    def learn_trick(self, trick):
        self.tricks.append(trick)
    def bark(self):
        print(f"{self.name} says woof")
    def perform_trick(self, trick):
        if(trick in self.tricks):
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} doesn't know {trick}")

husky = Dog("Otter", "Husky", 78664)

print(type(husky))
print(isinstance(husky, Dog))

husky.learn_trick("Sit")

print(husky.tricks)
husky.bark()