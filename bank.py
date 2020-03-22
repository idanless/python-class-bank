class BankAccount:
    bank_name = "Paybank"

    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def print_out(self,name):
        print("your balace is:" , name, self.balance)





idan = BankAccount()
idan.deposit(100)
idan.withdraw(50)

print("the bank is :" ,idan.bank_name)
print( idan.print_out('idan'))


