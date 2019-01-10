first_name = input("What is your first name? ")
print("hello, ", first_name)

# if else condition in python
if first_name == "Zakwan":
	print(first_name, "is learning Pyhton")
elif first_name == "Shehjad":
	print(first_name, "is learning C++")
else:
	age = int(input("What's your Age?  "))
	# if inside if with user input
	if age <= 6:
		print("wow! you are just {}! If you are confident and can read go ahead. ".format(age))
	print("You should totally learn Python {}".format(first_name))
# end here

print("have a great day {}".format(first_name))
print("Python is easy")
	
