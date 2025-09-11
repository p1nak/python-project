class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"Account '{self.name}' is created!\n Balance : ${self.balance : .2f}")

    def GetBalance(self):
        print(f"Account '{self.name}' \n Balance : ${self.balance : .2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit is complete.")
        self.GetBalance()

    def viableTransaction(self , amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account only has a balance of ${self.balance : .2f} ")

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.GetBalance()
        except BalanceException as error :
            print(f"\n Withdraw interrupted : {error}")

    def Transfer(self, amount, account):
        try:
            print("\n ********** \n\n Beginning transfer.....🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete. ✅ \n\n ********** ")
        except BalanceException as error:
            print(f"\n Transfer interrupted. {error}")

class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Depodite complete.")
        self.GetBalance()

class savingAcc(InterestRewardAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount +self.fee)
            print("\n Withdraw complete.")
            self.GetBalance()
        except BalanceException as error :
            print(f"\n Withdraw interrupted : {error}")

pinak = BankAccount(100, "pinak")
shiv = BankAccount(100, "shiv")

pinak.GetBalance()

pinak.deposit(100)

pinak.withdraw(20)

pinak.Transfer(50, shiv)

abhi = InterestRewardAcc(1000, "abhi")

abhi.GetBalance()

abhi.deposit(100)

abhi.Transfer(1000, pinak)

pinak.GetBalance()

blaze = savingAcc(1000, "blaze")

blaze.GetBalance()

blaze.deposit(100)

blaze.Transfer(200, pinak)
