def yell(text):
	text = text.upper()
	number_of_charecter = len(text)
	# // is use for get result in INTERGER value 
	result = text + "!" * (number_of_charecter // 2)
	print(result)

yell("You are doing great!")
yell("Don't forget to ask for help")
yell("Don't repeat yourself! KEEP THINGS DRY")

# praise = "You are doing great!"
# praise = praise.upper()
# number_of_charecter = len(praise)
# # // is use for get result in INTERGER value 
# result = praise + "!" * (number_of_charecter // 2)
# print(result)

# advice = "Don't forget to ask for help"
# advice = advice.upper()
# number_of_charecter = len(advice)
# result = advice + "!" * (number_of_charecter // 2)
# print(result)

# advice2 = "Don't repeat your self. KEEP THINNGS DRY"
# advice2 = advice2.upper()
# number_of_charecter = len(advice2)
# result = advice2 + "!" * number_of_charecter(number_of_charecter // 2)
# print(result)