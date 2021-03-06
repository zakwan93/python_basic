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


def display_whislist(display_name, wishes):
	# .copy method is used to create a copy of our list 
	items = wishes.copy()
	print(display_name + ": ")
	suggested_gift = items.pop(0)
	print("=====>", suggested_gift , "<=====")
	for item in items:
		print("* " + item)
	print()


display_whislist("Books", books)
display_whislist("Video Games", video_games)
