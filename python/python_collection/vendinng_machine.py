soda = ["Pepsi","Coke", "Sprite", "Dew"]
chpis = ["Lays","Doritos", "Pringles"]
candy = ["Snickers","Kit-Kat","Bounty","Twix"]

while True:
	choice = input("would you liek a SODA, CHIPS or CANDY ? ").lower()
	try:
		if choice == "soda":
			snack = soda.pop()
		elif choice == "chips":
			snack = chips.pop()
		elif choice == "candy":
			snack = candy.pop()
		else:
			print("Sorry, I don't understand that! ")
			continue
	except IndexError:
		print("We are all out of {}! Sorry!".format(choice))
	else:
		print("Here's your {}: {}".format(choice,snack))