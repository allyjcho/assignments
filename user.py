class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    def make_deposit(self,amount):
        self.account += amount
    def make_withdrawal(self,amount):
        self.account -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account}")
    def transer_money(self,other_user,amount):
        other_user.account += amount
        self.account -= amount

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

guido = User("Guido van Rossum","guido@python.com")
monty = User("Monty Python","monty@python.com")
ally = User("Ally Cho","allyjcho@gmail.com")

acc1 = BankAccount(0.02,1000)
acc2 = BankAccount(0.02,10000)

print(guido.account)

# guido.make_deposit(150).make_deposit(50).make_deposit(500).make_withdrawal(10).display_user_balance()

# monty.make_deposit(300).make_deposit(20).make_withdrawal(100).make_withdrawal(5).display_user_balance()

# ally.make_deposit(1000).make_withdrawal(500).make_withdrawal(50).make_withdrawal(600).display_user_balance()

# guido.transer_money(ally,2000)
# ally.display_user_balance()
# guido.display_user_balance()