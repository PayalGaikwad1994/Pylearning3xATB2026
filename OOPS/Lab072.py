#sum of digits in number Recursion

n=int(input("Enter a number"))

def sumofdigits(n):
    if n<10:
        return n
    else:
        return n%10 + sumofdigits(n//10)



print(sumofdigits(n))