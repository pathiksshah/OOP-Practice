#Python class called BankAccount which represents a bank account
class BankAccount():
    #constructor with parameters: accountNumber, name, balance
    def __init__(self,a,n,b):
        self.accountNumber = a
        self.name = n
        self.balance = b
    #Deposit() method which manages the deposit actions
    def Deposit(self,d):
        self.balance = self.balance + d
    #Withdrawal() method  which manages withdrawals actions
    def Withdrawal(self,w):
        self.balance = self.balance - w
    #bankFees() method to apply the bank fees with a percentage of 5% of the balance account
    def bankFees(self):
        self.balance = self.balance * 0.95
    
    def display(self):
        print(f"Account No:{self.accountNumber} \nAccount Owner: {self.name} \nCurrent Balance: {self.balance}")

newAccount = BankAccount(2178514584, "Tom" , 2700)
newAccount.Withdrawal(300)
newAccount.Deposit(200)
newAccount.display()