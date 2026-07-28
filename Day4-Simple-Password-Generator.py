import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Rand Letters
randLetters = ""
for i in range(1,nr_letters +1):
    randLetters += random.choice(letters)


# Rand Symbols
randSymbols = ""
for i in range(1,nr_symbols +1):
    randSymbols += random.choice(symbols)

# Rand Numbers
randNumbers = ""
for i in range(1,nr_numbers +1):
    randNumbers += random.choice(numbers)

randChars = list(randLetters + randSymbols + randNumbers)

#shuffle characters from a list and joins them into a single string
random.shuffle(randChars)
pwd = ''.join(randChars)

print(pwd)
