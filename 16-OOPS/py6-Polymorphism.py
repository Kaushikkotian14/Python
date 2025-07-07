class Animal:
    def sound(self):
        print("General sound of animal")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

for a in (Dog(),Cat()):  #[] can also works in place of ()
    a.sound()