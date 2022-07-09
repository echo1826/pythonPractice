# init is automatically called sort of like a constructor in JavaScript
# self is like this in JavaScript

class Puppy:
    def __init__(self, name):
        self.name = name
        self.tricks = []


puppy_obj = Puppy("Name")
print(puppy_obj.name)
print(puppy_obj.tricks)