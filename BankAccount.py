class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

jack = BankAccount(0.01,100)
jill = BankAccount(0.01,1000)

jack.deposit(1000).deposit(500).deposit(1200).withdraw(2500).yield_interest().display_account_info()
jill.deposit(1000).deposit(1000).withdraw(800).withdraw(800).withdraw(800).withdraw(800).yield_interest().display_account_info()
