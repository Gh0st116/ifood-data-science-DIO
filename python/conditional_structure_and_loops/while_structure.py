option = -1

while option != 0:
    option = int(input("[1] Withdraw \n[2] Bank Statement \n[0] Exit \n: "))

    if option == 1:
        print("Withdrawing...")
    elif option == 2:
        print("Getting bank statement...")
    else:
        print("Thanks for using our system, see you soon!")
