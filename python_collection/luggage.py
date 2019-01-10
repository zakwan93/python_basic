# ** Python will pack whatever keyword come into arguments 

# name none will take out from arguments and didn't pack it
def packer(name = None, **kwargs):
	print(kwargs)

packer(name="Zakwan",num = 23, spanish_inquisition="none")

def unpacker(first_name = None, last_name = None):
	if first_name and last_name:
		print("Hi {} {}".format(first_name,last_name))
	else:
		print("Hi no name!")

unpacker(**{"first_name": "Zakwan", "last_name": "Bhaiyat"})




# Challange_1
# You've used the string .format() method before to fill in blank placeholders.
# If you use a placeholder of {food} in the string, 
# then you pass a keyword argument of food to .format().
# The {food} placeholder in the string will be replaced with the value of the food 
# keyword argument.

# "Hi, I'm {name} and I love to eat {food}!".format(name="Kenneth", food="tacos")
# Returns "Hi, I'm Kenneth and I love to eat tacos!"
# Complete the favorite_food function below. It accepts a dictionary as an argument. 
# Your function should unpack that dictionary and pass it to the format 
# method as keywords, then return the resulting string.

def favorite_food(dict):
    return ("Hi, I'm {name} and I love to eat {food}!".format(**dict))

favorite_food({"name":"Kenneth","food":"tacos"})