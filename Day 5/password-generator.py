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
password = ""
for char in range(1, nr_letters + 1):
  randletter = random.choice(letters)
  password += randletter


for char in range(1, nr_symbols + 1):
  randsymbol = random.choice(symbols)
  password += randsymbol


for char in range(1, nr_numbers + 1):
  randnumber = random.choice(numbers)
  password += randnumber
print(f"Your password is: \n{password}")

#Hard Level - Order of characters randomised:
#This part has connection with easy level part
password_3 = ""
password_list = list(password) #converts the string into list
random.shuffle(password_list)

for char in password_list:
    password_3 += char

print(f"But I recommend you this password:\n{password_3}\nHope you'll get why I recommended this pass!")

#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P