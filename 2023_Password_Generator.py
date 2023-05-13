import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator")
your_letters=int(input("How many letters would you like in your password?:\n "))
your_symbols=int(input("How many symbols would you like?: \n"))
your_numbers=int(input("How many numbers would you like?: \n"))
password=[]
for letter in range(1,your_letters + 1):
    random_character=random.choice(letters)
    password.append(random_character)


for sym in range(1,your_symbols + 1):
    random_symbol=random.choice(symbols)
    password.append(random_symbol)

for num in range(1,your_numbers + 1):
    random_number=random.choice(numbers)
    password.append(random_number)


random.shuffle(password)
final_password="".join(password)

print(f"Your new password is: {final_password}")



    



    






    
    
    
    
    