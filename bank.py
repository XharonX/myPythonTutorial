from Account import *
from random import randint
from data_connection import connectDB
# from authenticate import Authenticate
class Bank:
    def __init__(self) -> None:
        self.accDB = {}
        self.nextAccountNumber = 0
    
    def createAccount(self, get_ID, accName, firstDepoist, Password):
        objAccount = Account(get_ID, accName, Password, firstDepoist)
        Bank_DB = connectDB('Account.db')
        # self.accDB.update(objAccount)
        Bank_DB.createTable()
        Bank_DB.Update(objAccount)
        print(self.accDB)

    def _getID(self):
        accID = int(randint(1000, 9999))
        if accID in self.accDB.values():
            for i in self.accDB.get('accountID'):
                if i == accID:
                    accID = int(randint(1000, 9999))
        return accID
    
    def openAccount(self):
        print()
        print("* * *  O P E N   A C C O U N T  * * *")
        print()
        print('# # # # # # # # # # # # # # # # # # # # # #')
        print()
        inputName = input("What is your name?\n\t:")
        startMoney = int(input("How much money do you want to deposit into the bank?\n\t"))
        while startMoney <= 0:
            startMoney = int(input("How much money do you want to deposit into the bank?\n\t:"))   
        password = input("Enter your secret password: ")
        accountNumber = self._getID()
        print(accountNumber)
        self.createAccount(accountNumber, inputName, startMoney, password)
        # self.accDatabase['accountID'] = accountNumber
        # self.accDatabase['accountName']= inputName
        # self.accDatabase['balance'] = inputstartMoney
        # self.accDatabase['password'] = password
        print("Your Account Number is -> %d." %accountNumber)

    def closeAccount(self):
        print()
        print("* * *  C L 0 S E   A C C O U N T  * * *")
        print()
        print('# # # # # # # # # # # # # # # # # # # # # #')
        print()

        userAccountName = input("What is your name?\n\t:")
        AccountID = int(input("Enter your Account ID: "))
        userPassword = input("   Enter your password: ")
        oAccount = Account(AccountID, userAccountName, userPassword)
        if self.auth(AccountID, userAccountName, userPassword):
            balance = oAccount.balance
            if balance is not None:
                print("You had ", balance,"in your account, which is being returned to you. ")
                # del self.accDatabase[oAccount] to delete this account within database.
                print("Your account has been closed.")
        else:
            print("You entered acount name or password was wrong. Please try later.")
            return None
    
    def deposit(self):
        print('* * *  D E P 0 S ! T  * * * ')
        accountNum = input('Please enter the account number: ')
        accountNum = int(accountNum)
        depositAmount = input('Please enter amount to deposit: ')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNum]
        theBalance = oAccount.deposit(depositAmount,
        userAccountPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)
    
    def withdraw(self):
        print('* * *  W ! T H D R A W  * * *')
        accountNum = int(input('Please enter the account number: '))
        withdrawAmount = int(input('Please enter amount to deposit: '))
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNum]
        if self.auth(accountNum, userAccountPassword):
            theBalance = oAccount.withdraw(withdrawAmount)
        else:
            print('You are in unauthorized person. Failed to login.')

        if theBalance is not None:
            print('Your withdraw amount is: ', withdrawAmount)
            print('Your new balance is:', theBalance)
    
    def menu():
        print("", end=' ')
        print('_ '*24)
        print("| Press an option to choose your oppontinity.")
        print("| [1] Open an account")
        print("| [2] Withdraw")
        print("| [3] Deposit")
        print("| [4] Close Account ")
        print("| [q] Quit")
        print(" ", end="")
        print('_ '*24)




if __name__ == '__main__':
    while True:
        AYA = Bank()
        Bank.menu()
        opt = input('Select an option: ')
        if opt == '1':
            AYA.openAccount()
        elif opt == '2':
            AYA.deposit()
        elif opt == '3':
            AYA.withdraw()
        elif opt == '4':
            AYA.closeAccount
        elif opt == 'q':
            quit()
        # import os
        # if print(os.getcwd()[-4:]) != 'bank':
        #     os.chdir('bank')

        # else:
