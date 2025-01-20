#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwd_list = []
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for num in range(0, nr_letters):
    passwd_list.append(random.choice(letters))

for num in range(0, nr_symbols):
    passwd_list.append(random.choice(symbols))

for num in range(0, nr_numbers):
    passwd_list.append(random.choice(numbers))
#print(passwd_list)

random.shuffle(passwd_list)
#print(passwd_list)


password = ""
for i in passwd_list:
    password+= i

print(f"your password is {password}")
