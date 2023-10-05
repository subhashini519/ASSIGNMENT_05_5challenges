class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
       
        self.balance -= amount

    def deposit(self, amount):
    
        self.balance += amount

    def getBalance(self):
      
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        
        return (self.balance * self.interestRate) / 100

acc_holder_name = input("Enter Account holder name:")
acc_balance = int(input("Enter account balance:"))
interest_rate = float(input("Enter interest rate:"))

demo1 = SavingsAccount(acc_holder_name,acc_balance,interest_rate)

deposit_amount = int(input("Enter the amount to be deposited:"))
demo1.deposit(deposit_amount)
print("Current Balance after  deposit   :", demo1.getBalance()) 

withdrawal_amount = int(input("Enter the amount to be withdrwn:"))
demo1.withdrawal(withdrawal_amount)
print("Current Balance after  withdrawal:", demo1.getBalance()) 

interest = demo1.interestAmount()
print("Interest Amount :", interest) 
