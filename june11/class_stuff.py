class BankAccount:

    def __init__(self,account_holder) -> None:
        self.account_holder=account_holder
        self.balance=0

    def withdrawl(self,amount):
        if amount>self.balance:
            print(f"Sorry your balance is {self.balance} you don't have enough funds")
        else:
            self.balance-=amount
            return self.balance
        

    def deposit(self,amount):
        self.balance+=amount

paul_account=BankAccount("paul")
paul_account.deposit(200)



renee_account=BankAccount("Renee")
renee_account.deposit(1000)
renee_account.withdrawl(999)
print(renee_account.balance)



        
    