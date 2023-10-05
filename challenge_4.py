class Account:
    def __init__(self, title, balance):
       
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        
        self.interestRate = interestRate

acc_holder_name = input("Enter Account holder name:")
acc_balance = int(input("Enter account balance:"))
interest_rate = float(input("Enter interest rate:"))
account = Account(acc_holder_name,acc_balance)
savings_account = SavingsAccount(acc_holder_name,acc_balance,interest_rate)


print("Account Title  :", account.title)
print("Account Balance:", account.balance)

print("Savings Account Title:", savings_account.title)
print("Savings Account Balance:", savings_account.balance)
print("Savings Account Interest Rate:", savings_account.interestRate)
