while True:
    option = int(input("Type a number: "))

    if option % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if option == 10:
        break

for number in range(100):
    if number == 10:
        break

    print(number, end=" ")
