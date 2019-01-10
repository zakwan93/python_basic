# Question.1
# Here is a multi-dimensional list of musical groups. 
# The first dimension is group, the second is group members.

# Can you loop through each group and output the members joined together 
# with a ", " comma space as a separator, please?


# Question.2
# can you please only print out the trios? 
# It should still use the joined string format from task 1



musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]

# Answer.1
for group in musical_groups:
	# Answer.2
	if len(group) == 3:
    	print(", ".join(group))

