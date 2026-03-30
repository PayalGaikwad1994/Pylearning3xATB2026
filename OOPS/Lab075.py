class Clac:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b


objRef=Clac(1,2)
print(objRef.sum())
print(objRef.sub())
print(objRef.mul())
print(objRef.div())


objref2 =Clac(int(input("Enter number A")),int(input("Enter number B")))
print(objref2.sum())
print(objref2.sub())
print(objref2.mul())
print(objref2.div())