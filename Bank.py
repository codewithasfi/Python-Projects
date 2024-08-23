# class Bank-
#     fields-acc_no
#            name 
#            balance
#     methods-withdraw
#             deposit
#             displayDetails

class noBalance(Exception):
    pass

class Bank:
    def __init__(self, accNo, n, bal):
        self.acc_no=accNo
        self.name=n
        self.balance=bal

    def withdraw(self):
        self.amount=int(input("Enter amount to withdraw:"))
        try:
            if (self.balance>self.amount):
                self.balance=self.balance-self.amount
                print("Amount withdrawn successfully.")
            else:
                raise noBalance
              
        except noBalance:
              print("Insufficient balance.")

        finally:
             print("Current Balance:",self.balance)
    
    def deposit(self):
        self.amount=int(input("Enter amount to deposit:"))
        try:
            if (self.amount<=10000):
                self.balance=self.balance+self.amount
                print("Amount deposited successfully.")
            else:
                raise Exception
            
        except Exception:
            print("Amount exceeded. Cannot deposit more than 10000.")

        finally:
            print("Current Balance:",self.balance)

    def displayDetails(self):
        print("Account number:",self.acc_no)
        print("Name:",self.name)
        print("Current Balance:",self.balance)
       

icici=Bank(101,"Asfiya Shaikh",50000)
icici.displayDetails()
icici.withdraw()
icici.deposit()

