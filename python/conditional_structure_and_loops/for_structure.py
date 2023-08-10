text = input("Type a text: ")
VOWELS = "aeiou"

# Iterating array
for letter in text:
    if letter.lower() in VOWELS:
        print(letter, end=" ")
    else:
        print() # Line break
        
# Using range 
for number in range(0, 51, 5):
    print(number, end=" ")