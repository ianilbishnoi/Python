# Classes
class Dog:
  def __init__(self, name, age): # constructor to set name and age
    self.name = name
    self.age = age

  def bark(self): # self refers to the current object
    print("I am a dog")

roger = Dog("Roger", 20) # creating an object of Dog
print(roger.age)
print(roger.bark()) # gives None because bark() does not return anything
print(type(roger))

# inheritance
class Animal: # parent class
    def walk(self):
        print("Walking.....")

class Dog(Animal): # Dog inherits from Animal
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

roger = Dog("Roger", 20)

print(roger.age)
roger.bark()
roger.walk()
