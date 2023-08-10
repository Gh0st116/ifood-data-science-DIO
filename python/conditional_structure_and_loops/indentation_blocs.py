def withdraw(value):
    balance = 500
    
    if balance >= value:
        print("Value withdrawn!")
        print("Retrieve your money")
    
    print("Thanks for being our customer, have a good day!")

def deposit(value):
    balance = 500
    balance += value
    
    print(f"Deposited successfully, your balance is currently {balance} dollars")


withdraw(300)

deposit(150)    
