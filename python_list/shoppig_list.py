import os
# create a new empty shopping list 
shopping_list = []

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


def show_help():
	clear_screen()
	print("What should we pick up at the store?")
	print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' for see your shopping list. 
Enter 'REMOVE' to delete an nitem from your list.
""")


# create a function name add_to_list that declared a parameter name item 
def add_to_list(item):
	show_list()
	if len(shopping_list):
		position = input("Where should I add {}? \n"
			"Press ENTER to add to the end of the list \n"
			"> ".format(item))
	else:
		position = 0
	try:
		position = abs(int(position))
	except ValueError:
		position = None
	if position is not None:
		shopping_list.insert(position-1,item)
	else:
		# add item to list
		shopping_list.append(item)

	show_list()
	

# define a function show_list that print all the item in the list
def show_list():
	clear_screen()
	print("Here's your list")
	# Setting index = 1 beacuse list of item is start from one
	index = 1
	for item in shopping_list:
		print("{}. {}".format(index,item))
		index += 1

	# just added 10 dasesh at the end of list
	print("-"*10)

def remove_from_list():
	show_list()
	what_to_remove = input("What would you like to remove? \n > ")
	try:
		shopping_list.remove(what_to_remove)
	except ValueError:
		pass
	show_list()


show_help()
# infinete loop
while True:
	new_item = input("> ")

	if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
		break
	elif new_item.upper() == "HELP":
		show_help()
		continue
	# enable the SHOW command to show the list
	elif new_item.upper() == "SHOW":
		show_list()
		continue
	elif new_item.upper() == "REMOVE":
		remove_from_list()
	else:
		# call add_to_list with new_item as an argument  
		add_to_list(new_item)

show_list()