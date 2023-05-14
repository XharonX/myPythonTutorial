accountNameList = ['',]
accountBalanceList = ['',]
accountPasswordList = ['',]

def getAccountID(accountName):
    return accountNameList.index(str(accountName))

def accountCreate(accountname, password, balance):
    accountNameList.append(accountname)
    accountPasswordList.append(password)
    accountBalanceList.append(balance)
    return getAccountID(accountName=accountname)

def showDetail(accountID):
    name = accountNameList[accountID]
    balance = accountBalanceList[accountID]
    password = accountPasswordList[accountID]
    print('\t Name: ',name)
    print('\t Balance: ',balance)
    print('\t Password: ',password)

def menu():
    print()
    print('Press b to get the balance')
    print('Press c to create a new account')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

def deposit(accountID, accountName, depositAmount):
    if accountName in accountNameList and getAccountID(accountName) == int(accountID):
        if depositAmount < 0:
            print("Your deposit amount is invalid.")
            return 0
        else:
            accountBalanceList[accountID] += depositAmount
    else:
        result = "Your account ID and account Name are not match."
        print(result)
        return result

def withdraw(accountID, accountName, withdrawAmount):
    if accountName in accountNameList and getAccountID(accountName) == int(accountID):
        if withdrawAmount < 0:
            print("Your withdrawal amount is invalid")
            return 0
        elif withdrawAmount > accountBalanceList[accountID]:
            print("You cannot withdraw more than account Balance. Please check your amount")
            return 0
        else:
            accountBalanceList[accountID] -= withdrawAmount
    else:
        result = "Your account ID and account Name are not match."
        print(result)
        return result

def getBalance(accountID):
    balance = accountBalanceList[accountID]
    print('Your balance is: ', balance)
    return balance


while True:
    menu()
    option = input("Choose an option: ")
    option = option.lower()
    option = option[0]

    if option == 'b':
        getBalance(int(input("Enter your account ID: ")))
    elif option == 'c':
        ID = accountCreate(input("Enter account name: "), input("Enter password: "), int(input("Enter First deposit Balance: ")))
        print('Please read in mind your account ID. -> %d' %ID)
    elif option =='d':
        deposit(int(input("Enter your account ID: ")), input("Enter account name: "), int(input("Enter amount of deposit: ")))
    elif option == 'w':
        withdraw(int(input("Enter amount of withdraw: ")))
    elif option == 's':
        showDetail(int(input("Enter your accountID: ")))
    elif option == 'q':
        print('See You!')
        break
