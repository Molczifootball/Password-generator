#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
allthings = letters
allthings.extend(numbers)
allthings.extend(symbols)

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

eazy_letters = ""
eazy_numbers = ""
eazy_symbols = ""
hard_pass = []
for letter in range(0,nr_letters):
  let = letters[random.randint(0,len(letters)-1)]
  eazy_letters += str(let)
  hard_pass.append(let)

for number in range(0,nr_numbers):
  num = numbers[random.randint(0,len(numbers)-1)]
  eazy_numbers += str(num)
  hard_pass.append(num)

for symbol in range(0,nr_symbols):
  sym = symbols[random.randint(0,len(symbols)-1)]
  eazy_symbols += str(sym)
  hard_pass.append(sym)

eazy_pass = eazy_letters + eazy_numbers + eazy_symbols
print("EZ pass is: "+eazy_pass)

random.shuffle(hard_pass)

final_password = ""
for letter in hard_pass:
  final_password += letter

print("Hard pass is: "+final_password)
