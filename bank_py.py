class BankAccount:
    bankAcc = []
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.bankAcc.append(self)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n***Succesfully deposit {amount}***")
            print(f"***Your balance : {self.balance}***")
        else:
            print("Deposit unsuccessful. Amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"\n***Succesfully withdraw {amount}***")
            print(f"***Your balance : {self.balance}***")
        else:
            print("Withdraw unsuccessful. Amount must be positive.")
    
    def transfer(self, recipient_name, amount):
        recipient = None
        for account in BankAccount.bankAcc:
            if account.owner == recipient_name:
                recipient = account
                break
        
        if recipient is None:
            print("Incorrect transfer: recipient not found.")
        elif amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            recipient.balance += amount
            print(f"\n***Transfer successful. {amount} transferred to {recipient.owner}.***")
            print(f"***Your balance : {self.balance}***")
        else:
            print("Transfer unsuccessful. Amount must be positive.")
    
    def get_balance(self):
        return self.balance, self.number

acc2 = BankAccount("Diddy", 1000) # For test

def getInput():
    owner = input("Enter your bank account name : ")
    balance = float(input("Enter your balance : "))
    acc1 = BankAccount(owner, balance)
    while True:
        print("\nEnter number for your transaction :\n1.deposit\t\t2.withdraw\n3.transfer\t\t4.get balance\n\t5.End transaction\n")
        userInput = int(input("Enter your option : "))
        if userInput == 1:
            amount = float(input("Enter your deposit amount : "))
            acc1.deposit(amount)
        elif userInput == 2:
            amount = float(input("Enter your withdraw amount : "))
            acc1.withdraw(amount)
        elif userInput == 3:
            recipient_name = input("Enter your recipient's name: ")
            amount = float(input("Enter your transfer amount: "))
            acc1.transfer(recipient_name, amount)
        elif userInput == 4:
            print(f"***Your balance : {acc1.get_balance()}***")
        elif userInput == 5:
            print(f"\n***Thank you {owner}***\n")
            break
        else:
            print("Invalid input")

def main():
    getInput()

if __name__ == "__main__":
    main()