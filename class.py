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

husky = Dog("Otter", "Husky", 78664)

print(type(husky))
print(isinstance(husky, Dog))

husky.learn_trick("Sit")

print(husky.tricks)