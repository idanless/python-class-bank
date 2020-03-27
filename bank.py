class BankAccount:
    bank_name = "Paybank"

    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def print_out(self,name):
        print("your balance is:" , name, self.balance)

class Bank(BankAccount):
    def __int__(self,name1='y'):
        BankAccount.__init__(self,balance=0)
        self.name1 = name1

    def print_y(self, name1):
        print("your balance is:", name1,self.balance,self.bank_name)

idan = BankAccount()
idanname = Bank()
idanname.deposit(150)
idanname.withdraw(20)
idanname.print_y('idan')
idan.deposit(100)
idan.withdraw(50)
idan.bank_name = 'idan'
x = idan.balance
#print(str(x)+'\t'+str(idan.bank_name))
