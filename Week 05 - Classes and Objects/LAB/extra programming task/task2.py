class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")
        
    def birthday(self):
       self.age += 1

dog = Dog("Buddy", 3)

dog.bark()
print("Age before birthday: ", dog.age)

dog.birthday()
print("Age after birthday", dog.age)
