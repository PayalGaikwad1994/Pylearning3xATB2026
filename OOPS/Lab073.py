class Person:

    name = None
    age = None

    def walk(self):
        print("walk")

    def talk(self):
        print("talk")

    def __init__(self):
        print("Default Constructor")

sunidhi=Person()
sunidhi.name = "Sunidhi"
sunidhi.talk()

pooja=Person()
pooja.name = "Pooja"
pooja.walk()