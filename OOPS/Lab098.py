#Custom Exception

class myCustomException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)

balance=100

withdraw=int(input("Enter withdraw amount: "))

if withdraw>balance:
    raise myCustomException("Withdraw amount is greater than balance")
else:
    balance-=withdraw
    print("Remaining balance is:",balance)
