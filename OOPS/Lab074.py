class Dog:
    name= None
    id=None

    def __init__(self,name,id):
        self.name=name
        self.id=id

    # def __init__(self):
    #     print("Default contructor")

    def seeping(self):
        print(f'Who is sleeping -> {self.name}')



d1=Dog("Chaw",1)
d2=Dog("Maw",2)

print(f'{d1.name} has id {d1.id}')
print(f'{d2.name} has id {d2.id}')
d1.seeping()
d2.seeping()