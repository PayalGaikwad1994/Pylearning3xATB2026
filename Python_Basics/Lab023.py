#find maximum of two numbers

print(max(float(input("Enter number a\n")),float(input("Enter number b\n"))))

p=float(input("Enter a first number: "))
q=float(input("Enter a second number: "))

if p>q:
    print("maximum no. is:",p)
elif q>p:
    print("maximum no. is:",q)
else:
    print("Both are equal")

print("maximum no. is P" if p>q else "maximum no. is q" if q>p else "Both are equal")
