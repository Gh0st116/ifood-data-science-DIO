LEGAL_AGE = 18
SPECIAL_AGE = 12

age = int(input("Type your age: "))

if age >= LEGAL_AGE:
    print("You can have your driver's license!")
elif age >= SPECIAL_AGE:
    print("You can take theory classes, but can't drive yet.")
else:
    print("You are not old enough to have a driver's license.")
