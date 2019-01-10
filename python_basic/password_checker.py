import sys

MY_PASSWORD = "python"
password = input("Please enter your password:  ")

# use of while loop
attempt_count = 1

while password != MY_PASSWORD:
	if attempt_count > 3:
		sys.exit("Sorry you reached your attepmt! you're account has been blocked! ")
	password = input("Invalid password, try again:  ")
	attempt_count += 1
print("Welcome to my Python journy!")
	

# Use of for loop
my_name = "ZAKWAN"
for letter in my_name:
	print(letter.upper())



# Example to check if user unnderstand while loop if not keep asking until it understand 

name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops

ask_user = input(("{}, Do you unnderstand Python while loop ?  ").format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
while ask_user != "yes":
# TODO: Since the user doesn't understand while loops, let's explain them.
    print("While loop is use to repeat until the conndition match")
# TODO: Ask the user again, by name, if they understand while loops.
    ask_user = input(("{}, now you understand about while loop ?  ").format(name))
  
# TODO: Outside the while loop, congratulate the user for understanding while loops
 
print("Congrats, You understand WHILE loop")
