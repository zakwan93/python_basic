print("Hello, World!")

myDesret = "Chocolate" + " and Cookies"
print(myDesret)

desert = myDesret + ("!" * 20) 

myDesret += " and Cakes"
print(myDesret)

print(desert)

# How to get the length of string 
quote = "I'm learninng Python!"
print(len(quote))

# The way to use inbuild method of python on your object
# For ex. convert our string into Upper Case using inbuild method
print(quote).upper()

# All different innbuild methods
print(quote).lower()
print(quote).title()

# Place Holder in pyhton using FORMAT in build method 

# 1. The use of placeholder in Python
# - define place holder usinng {} 
subject_template = "Thanks for learning {} with us {}!"

# 2. use .format method with arguments
print(subject_template.format("Python","Zakwan"))
print(subject_template.format("React","Zakwan"))

# 3. Iline use of .format method with different datatypes
print("You just learned {} different {}").format(4,"Inbuild method")

# //Another method call IN to check the word is presennt in string 
print("Zakwan" in "subject_template") 
# Output- False because we are checkinng in actual subject_template strig
print("Thanks" in subject_template)
# Output- True 