import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Easy version
easy_password = ""
hard_password = []
for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    easy_password += random_letter
    hard_password.append(random_letter)

for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    easy_password += random_symbol
    hard_password.append(random_symbol)

for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    easy_password += random_number
    hard_password.append(random_number)

print("Easy Password: " + easy_password)

random.shuffle(hard_password)
final_hard_password = ""
for shuffled_password in hard_password:
    final_hard_password += shuffled_password
print("Hard Password: " + final_hard_password)