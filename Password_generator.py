#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

el =  len(letters)
en =  len(numbers)
es =  len(symbols)

password = ""
for letter in range(nr_letters):
    randletter = (random.randint(0, el-1))
    password += letters[randletter]

for number in range(nr_numbers):
    randnumbeer = (random.randint(0, en-1))
    password += numbers[randnumbeer]

for symbol in range(nr_symbols):
    randsymbol = (random.randint(0, es-1))
    password += symbols[randsymbol]
print(f"Your Eazy level password is : {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password1 = ""
for letter in range(nr_letters):
    randletter = (random.randint(0, el-1))
    password1 += letters[randletter]

for number in range(nr_numbers):
    randnumbeer = (random.randint(0, en-1))
    password1 += numbers[randnumbeer]

for symbol in range(nr_symbols):
    randsymbol = (random.randint(0, es-1))
    password1 += symbols[randsymbol]

password_list = list(password1)
random.shuffle(password_list)
password2 = ''.join(password_list)
  
print(f"Your Hard level password is : {password2}")
