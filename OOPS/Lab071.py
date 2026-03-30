# Recursion
# Recursion is a programming technique where a function
# calls itself in order to solve a problem.


# Key Concepts
# 1. Base Case
# 2. Recursive Case

#Factorial

def recursion(n):

    #Base case when n reaches to 1 or 0
    if n == 0 or n == 1:
        return 1
    else:
        return n *recursion(n-1)



print(recursion(5))