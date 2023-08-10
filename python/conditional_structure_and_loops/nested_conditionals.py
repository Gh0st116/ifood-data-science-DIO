regular_account = True
student_account = False
special_account = False

balance = 2000
withdrawal = 500
overdraft = 450

if regular_account:
    
    if balance >= withdrawal:
        print("Withdrawn successfully")
    elif withdrawal <= (balance + overdraft):
        print("Withdrawn with overdraft")
        
elif student_account:
    
    if balance >= withdrawal:
        print("Withdrawn successfully")
    else:
        print("Insufficient balance")

elif special_account:
    print("Special account selected!")

else :
    print("Invalid account type")
