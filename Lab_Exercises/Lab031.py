#factorial

n=int(input("Enter a number"))
fact=1

while n>=1:
    fact=fact*n
    n=n-1

print(fact)

for i in range(1,n+1):
    fact=fact*i

print(fact)