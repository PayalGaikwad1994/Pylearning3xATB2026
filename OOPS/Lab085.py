#Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("BHK1")

class Payal(Father):
    def BHK2(self):
        print("BHK2")

class Komal(Father):
    def BHK3(self):
        print("BHK3")

class Santosh(Father):
    def BHK4(self):
        print("BHK4")


payal=Payal()
payal.BHK1()
payal.BHK2()

komal=Komal()
komal.BHK1()
komal.BHK3()

santosh=Santosh()
santosh.BHK1()
santosh.BHK4()