# Overloading → same method name, different parameters
# Overriding → child class changes parent method behavior

class Demo:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


obj = Demo()
print(obj.add(2, 3))