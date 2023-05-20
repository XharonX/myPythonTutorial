class Account:
    def __init__(self, accID:int, name:str, password:str, balance:int):
        self.name = name
        self.password = password
        self.balance = balance
        self.accountID = accID


    def deposit(self, depoistAmount):
        if self.balance < 0:
            raise ValueError("Deposit Amount must not less than 0")
        self.balance += depoistAmount
        return self.balance
    
    def withdraw(self, withdrawAmount):
        if self.balance < 0:
            raise ValueError("Deposit Amount must not less than 0") 
        elif self.balance > self.balance:
            self.balance -= withdrawAmount
            return self.balance
    
    def getBalance(self, password):
        if self.password != password:
            print("Sorry, Incorrect Password")
            return 0
        return self.balance
    
    def details(self):
        print("\tName: %s" %self.name)
        print("\tBalance: %.1f" %self.balance)
        print("\tPassword: %s" %self.password)
    




# acc1 = Account("Ninux", "admin", 30000)
# acc2 = Account("Sin", "Yangon", 10000000)

# acc1.details()