class AmountExceeded(Exception):
    pass

class AmountLimit(Exception):
    pass

class Bank:
    def __init__(self):
        self.balance=int(input("Enter your balance:"))

    def withdraw(self):
        self.amount=int(input("Enter the amount to withdraw:"))
        try:    
            if self.amount<=self.balance:
                self.balance=self.balance-self.amount
                print("Amount withdrawn successfully. Current balance:",self.balance)
            else:
                raise AmountExceeded()
        
        except:
            print("Amount is more than balance.")

    def deposit(self):
        self.amount=int(input("Enter amount to deposit:"))
        try:
            if self.amount<=10000:
                self.balance=self.balance+self.amount
                print("Amount deposited successfully. Current balance:",self.balance)
            else:
                raise AmountLimit()

        except:
            print("Deposit limit is Rs.10000. Deposit not successful.")
b1=Bank()
b1.withdraw()
b1.deposit()
