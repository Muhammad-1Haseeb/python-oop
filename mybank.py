class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
    
    def deposite(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

acc = BankAccount("Haseeb", 1000)
print(acc.owner)
print(acc.get_balance())

acc.deposite(500)
print(acc.get_balance())

acc.withdraw(100)
print(acc.get_balance())

