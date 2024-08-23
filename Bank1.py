class Bank1:
    def __init__(self):
        self.accNo= int(input("Enter your acc number:"))
        self.name= input("Enter your name:")
        self.balance=int(input("Enter your balance:"))
    
    def withdraw(self):
        print("Withdraw.")
    
    def deposit(self):
        print("Deposit.")
    
    def display(self):
        print("Name:",self.name)
        print("AccNo:",self.accNo)
        print("Balance:",self.balance)

sbi = Bank1()
sbi.withdraw()
sbi.deposit()
sbi.display()
