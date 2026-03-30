class Car:
    name=None
    make=None
    model=None
    year=None

    def __init__(self,name,make,model,year):
        self.name=name
        self.make=make
        self.model=model
        self.year=year

    def start_engine(self):
        print(self.name,self.make,self.model,self.year)


lamo=Car("Lmborgini","2024","v2","XXX")
lamo.start_engine()