#triangle classifier

side1=float(input("Enter the side 1: "))
side2=float(input("Enter the side 2: "))
side3=float(input("Enter the side 3: "))

if side1==side2==side3:
    print("Triangle is Equilateral")
elif side1==side2 or side2==side3 or side3==side1:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")