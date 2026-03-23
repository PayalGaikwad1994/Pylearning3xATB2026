#Lambda expression for even odd

def chk_even_odd(num):
    if num %2==0:
        print("Given number is even")
    else:
        print("Given number is odd")

num=int(input("Enter a number:"))
chk_even_odd(num)

#with Lambda expression

chk_odd_even=lambda num: print("even") if num%2==0 else print("Odd")
chk_odd_even(num)

chk_odd_even1=lambda num: "even" if num%2==0 else "Odd"
print(chk_odd_even1(num))
