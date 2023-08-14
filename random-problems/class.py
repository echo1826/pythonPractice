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
    # class attribute, attributes not defined in an instance method, defined on the class itself
    # class attributes means all objects will have this attribute with this value
    species = 'canine'

    def __init__(self, name, breed, location):
        # instance attributes attributes defined inside of the instance method (i.e. self.name  )
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    @classmethod
    def register_stray(cls):
        # cls represents the actual Dog class, or class the class method is defined on
        print(cls)
        return cls('coming soon', 'unknown', 'unknown')

    def whine(self):
        print("whine")

    def learn_trick(self, trick):
        if(trick not in self.tricks):
            self.tricks.append(trick)
        else:
            print(f"{self.name} already knows {trick}")
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

print(husky.species)
print(Dog.species)

stray = Dog.register_stray()
print(stray.name, stray.location, stray.breed)

class Cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name} meows")

# how to make a sub class/inherit another class methods and attributes
class Lion(Cat):
    def __init__(self, name, pride_name):
        # this is how to super the parent class attributes before initiating the specific attributes for the child class
        # same super as JavaScript, just have to attach the init method passing in the parent attribute needed to construct the class
        super().__init__(name)
        self.pride_name = pride_name
    def roar(self):
        print(f"{self.name} roars")