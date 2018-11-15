# importing inbuil math library into our code.
# So we can now call different math method in our function
import math

def split_check(total, number_of_people):
	if number_of_people <= 1: 
		raise ValueError("More than 1 person is required to split the bill ...") 
	# This answer will give you float value

	# cost_per_person = total / number_of_people

	# But to make it in round figure in nearest integer we can use math CEIL method
	# cost_per_person = math.ceil(total / number_of_people)

	# here wew assign result in one varrible and then return it
	# but we are using math function with in build method it will return by itself
	# That means we don't have to assign this to any varriable and return it
	# so comment out next line

	# return cost_per_person
	return math.ceil(total / number_of_people)

# using TRY and EXCEPT for exception value 
try:
	total_due = float(input("What is the total ?  "))
	num_of_people = float(input("How many people ?  "))
	amount_due = split_check(total_due,num_of_people)

# ValueError is the error name 
# This is without as which is also work
# except ValueError :
# 	print("Oh SNAP! I Guess you are way too much drunk! ")
	# print the error usin AS method
except ValueError as err:
	print("Oh SNAP! I Guess you are way too much drunk! ")
	print("({})".format(err))

else:
	print("Each person owes ${}".format(amount_due))


