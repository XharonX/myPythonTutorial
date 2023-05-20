import sqlite3
import os


class connectDB():
    UNIQUE_TABLE = 'BankAccount'
    def __init__(self, dbName) -> None:
        self.dbName = dbName
        print(os.getcwd())
        if os.path.exists('bank'):
            os.chdir('bank')
        if os.path.exists('db'):
            os.chdir('db')
        print(os.getcwd())
        self.conn = sqlite3.connect(os.getcwd()+'/%s' %self.dbName)
        self.c = self.conn.cursor()

    def createTable(self, tableName=UNIQUE_TABLE):
        try:
            self.c.execute("CREATE TABLE BankAccount (accountID INTEGER PRIMARY KEY, accountName TEXT, password TEXT, balance INTEGER) ")

            self.c.execute("SELECT BankAccount FROM Account WHERE type='table' AND name='BankAccount'")
            result = self.c.fetchone()
            if result:
                print("{tableName} has been created. ")
                return None
            else:
                pass
                # create a table
        # except sqlite3.OperationalError(args='')
                # self.c.execute("CREATE TABLE BankAccount (accountID INTEGER PRIMARY KEY, accountName TEXT, password TEXT, balance INTEGER) ")
        except:
            print("Do something")

        finally:
            self.conn.commit()
            # self.conn.close()

    def queryTable(self):
        self.c.execute("SELECT * FROM BankAccount ")
        results = self.c.fetchall()
        for row in results:
            print(row)

    def Update(self, oAccount):
        self.c = self.conn.cursor()
        data = (oAccount.accountID, oAccount.name, oAccount.password, oAccount.balance)
        self.c.execute('INSERT INTO BankAccount (accountID, accountName, password, balance) VALUES (?, ?, ?, ?)' , data)
        self.conn.commit()
        self.conn.close()