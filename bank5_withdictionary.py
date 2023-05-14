# acc = [
#     {
#         'name': 'Ninux',
#         'balance': 2000,
#         'id': 2421,
#         'password': 'admin'
#     },
#     {
#         'name': 'Charon',
#         'balance': 2000,
#         'id': 2114,
#         'password': 'hello'
#     }
# ]
# for ac in acc:
#     print( 'Ninux' in ac.values())
#     print(acc.index('Ninux' in ac.values()))
    
import random

accountList =[]

def generateID(userID):
    value = int(random.randint(1, 9))
    for user in accountList:
        if value in user.values():
            generateID(value)
        else:
            return value
        
def createAcc(name, balance, passwd):
    global accountList
    account = {
        'id': int(generateID()), # ID may be leap with random.randint(1000, 9999)
        'name': name,
        'balance': balance,
        'password': passwd
        }
    accountList.append(account)
    return account['id']


def getBalance(ID):
    print(ID)
    for acc in accountList:
        if id in acc.values():
            balance = acc.get('balance')
            print("Your main balance is: %d" %balance)
        else:
            print('Your entered ID is a wrong number(ID).')
            return None
        return None

def accountDeposit(accountID, accountName, accountDeposit):
    for user in accountList:
        if accountID in user.values() and accountName in user.values():
            pass
        else:
            continue

        name = user.get('name')
        id = user.get('id')
        if accountID == id and accountName == name:
            if accountDeposit < 0:
                print("Your deposit amount is invalid.")
                return 0
            else:
                user['balance'] += accountDeposit
                return user['balance']
    else:
        print("Your ID hasn't been found. Please Try again.")
        return None


def accountWithdraw(accountID, accountName, accountWithdraw):
    for user in accountList:
        if accountID in user.values() and accountName in user.values():
            pass

        else:
            continue
        name =user.get('name')
        id = user.get('id')
        if accountID == id and accountName == name:
            if accountWithdraw < 0:
                print("Your withdrawal amount is invalid")
                return 0
            elif accountWithdraw > user['balance']:
                print("You cannot withdraw more than account Balance. Please check your amount")
                return 0
            else:
                user['balance'] -= accountWithdraw
                return  user['balance']
        else:
            print("Your ID number and account name are not match.")
            return None
    else:
        print("Your account ID or Name hasn't been found. Please Try again.")
        return None


def showDetails(accountID, accountName):
    for user in accountList:
        if accountID in user.values() and accountName in user.values():
            for key, value in user.items():
                print("\t#{0} -> {1} <<".format(key, value))
        else:
            continue
    else:
        print("Your account ID or Name hasn't been found. Please Try again.")
        return None

def menu():
    print()
    print('Press b to get the balance')
    print('Press c to create a new account')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

def chooseOption():
    option = input("Choose an option: ")
    option = option.lower()
    return option[0]



while True:
    menu()
    option = chooseOption()
    if option == 'b':
        getBalance(input("Enter ID: "))

    elif option == 'c':
        id = createAcc(
            input('What is your name?\n'), int(input("Please enter your first deposit amount: ")), input("Please enter your password: ")
            )
        print("Plese remain your ACCOUNT ID is:-> %d" %id)
    
    elif option == 'd':
        accountDeposit(int(input('Enter ID number: ')), input("Enter account name: "), int(input("Please Deposit amount: ")))

    elif option == 'w':
        accountWithdraw(int(input('Enter ID number: ')), input("Enter account name: "), int(input("Please Withdraw amount: ")))
    elif option == 's':
        showDetails(int(input('Enter ID number: ')), input("Enter account name: "))
    elif option == 'a':
        for a in accountList: print(a)

