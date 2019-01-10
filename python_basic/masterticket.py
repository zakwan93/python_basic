TICKET_PRICE = 10
SERVICE_CHARGE = 2
ticket_remaining = 100

# create a calculate_price function. It take number of ticket annd return
def calculate_price(number_of_ticket):
	 return (number_of_ticket * TICKET_PRICE) + SERVICE_CHARGE
	 # create a new constant for 2 dollar ticket charge
	 


# Runn this code continuoslly will run out of tickets
while ticket_remaining >= 1:

	# Task 1 - Output how many tickets are remaining usig the ticket_remaining varrible

	print("There are {} tickets remaining".format(ticket_remaining))

	# Task 2 - Gather the users name and assign it to a new varrible

	user_name = input("Hey there, What's your name?  ")

	# Task 3 - prompt the user by name and ask how many tickets they would like to buy
	number_of_ticket = input("Welcome {}, How many tickets you would like to buy?  ".format(user_name))
	# EXPECT to value error to happen and handle it apropriatlly 
	try:
		number_of_ticket = int(number_of_ticket)
		# Raise a ValueError if the request is for more tickets then the available.
		if number_of_ticket > ticket_remaining:
			raise ValueError("There are only {} are remaining! ".format(ticket_remaining))  
	except ValueError as err:
		print("Oh NO! we ran into issue please. {}. Please try again! ".format(err))
	else:
		# Task 4 - Calculate the price (number of tickets * price ) and assign it to the varriable 
		# total = number_of_ticket * TICKET_PRICE

		# create a function for check total and add service charge to it
		total = calculate_price(number_of_ticket)

		# Task 5 - Output the price on screen
		print("Your total due is {} for {} tickets !  ".format(total,number_of_ticket))

		# Task 5 - prompt user if they want to proceed. Y/N
		confirm = input("You want to proceed? Please input Y / N   ")

		# Task 6 - if they want to proceed
		if confirm.lower() == "y":
			# Task 7 - Prinnt out ticket "SOLD" to confirm purchase
			# TODO: Gather Credit card innformation ad proceed it.
			print("Ticket SOLD! Thanks for purchase with us!  ")
			# Task 8 - Then decreament the ticket remaining by the number_of_ticket purchased 
			ticket_remaining -= number_of_ticket

		# Task 9 - Otherwise Exit and Thank you by name
		else:
			print("Well, Thank you anyway {}!  ".format(user_name))


# Notify user ticket sold out 
print("Sorry all ticket SOLD OUT {}! ".format(user_name))

