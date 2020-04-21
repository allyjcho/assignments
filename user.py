class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount

guido = User("Guido van Rossum","guido@python.com")
monty = User("Monty Python","monty@python.com")
ally = User("Ally Cho","allyjcho@gmail.com")

guido.make_deposit(150).make_deposit(50).make_deposit(500).make_withdrawal(10).display_user_balance()

monty.make_deposit(300).make_deposit(20).make_withdrawal(100).make_withdrawal(5).display_user_balance()

ally.make_deposit(1000).make_withdrawal(500).make_withdrawal(50).make_withdrawal(600).display_user_balance()

guido.transer_money(ally,2000)
ally.display_user_balance()
guido.display_user_balance()