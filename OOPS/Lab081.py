#Poor example of encapsulation

class BankAccount:
    def __init__(self,balance):
        self.balance=0
        self.__private_var="123"

    def access_private_var(self):
        print("Private variable accesses",self.__private_var)

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def print_balance(self):
        print("Your Balance is",self.balance)

account_holder=BankAccount(100)
account_holder.access_private_var()
account_holder.deposit(100)
account_holder.print_balance()
account_holder.withdraw(50)
account_holder.deposit(100)
account_holder.print_balance()
