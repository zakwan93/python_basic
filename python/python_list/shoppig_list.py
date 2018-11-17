# create a new empty shopping list 
shopping_list = []

def show_help():
	print("What should we pick up at the store?")
	print("""
Enter DONE to stop adding items.
Enter HELP for this help.
Enter SHOW for see your shopping list. 
""")


# create a function name add_to_list that declared a parameter name item 
def add_to_list(item):
	# add item to list
	shopping_list.append(item)
	# notify user that item was added and state the number of items in the list curruntlly 
	print("{} has been added to the list. List has {} items!".format(item,len(shopping_list)))
	

# define a function show_list that print all the item in the list
def show_list():
	print("Here's your list")
	for item in shopping_list:
		print(item)



show_help()
# infinete loop
while True:
	new_item = input("> ")

	if new_item == "DONE":
		break
	elif new_item == "HELP":
		show_help()
		continue
	# enable the SHOW command to show the list
	elif new_item == "SHOW":
		show_list()
		continue
	
	# call add_to_list with new_item as an argument  
	add_to_list(new_item)

show_list()