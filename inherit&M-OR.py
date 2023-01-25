class Animals:
    print("animals")

class Dog(Animals):
    def speak(self):
        print("bowbow")

class Cat(Animals):
    def speak(self):
        print("meom meom")

obj=Cat()
obj.speak()
