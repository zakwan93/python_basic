# run this file using    python3 -i filename     for interective mode 

books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

print("Books: ")
for book in books:
	print("*" + book)

	
# use of garbage_collector is to use garbage means the value which we donn't need
# any longer in our main object but we can assign that value to some varriable
# and can acces it later if we want 

# Assigning first value of books list to garbage_collector
garbage_collector = books[0]

# Deleting 1st value of list using del method 
del books[0]

# now 1st value of our list is nol onnger available in books varriable
# but we assign that value to garbage_collector before Deleting it
# we can actully use that value calling garbage_collector varriable 

print("suggested gift {}".format(books[0]))

# POP is use to remove item from list by default it removes last item of list
print(books.pop())

# but we can assign specific index to pop up from our list 
# This will delete 3 item from our list
print(books.pop(2))
print(garbage_collector)
print(books)



