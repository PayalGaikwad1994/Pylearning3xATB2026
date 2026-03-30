#Encapsulation

class BankAccount:
    def __init__(self):
        self.balance=0
        self.__private_var="123"

    def access_private_var(self):
        print("Private variable accesses",self.__private_var)

    def deposit(self,amount):
        self.balance=self.balance+amount

    def __withdraw(self,amount):
        self.balance=self.balance-amount

    def __print_balance(self):
        print("Your Balance is",self.balance)

    def if_you_are_auth(self,flag):
        if flag:
            self.__print_balance()
        else:
            print("You are not authorised")

    def if_you_are_auth_to_Withdraw(self, flag,amount):
        if flag:
            self.__withdraw(amount)
        else:
            print("You are not authorised")


JPChaser=BankAccount()
JPChaser.deposit(100)

secret_pass_balance=int(input("Enter the secret password to see Balance:"))
if secret_pass_balance==1234:
    JPChaser.if_you_are_auth(True)
else:
    JPChaser.if_you_are_auth(False)

secret_pass_withdraw=int(input("Enter the secret password to see Withdraw:"))
if secret_pass_withdraw==1234:
    JPChaser.if_you_are_auth_to_Withdraw(True,50)
    JPChaser.if_you_are_auth(True)
else:
    JPChaser.if_you_are_auth_to_Withdraw(False,50)

