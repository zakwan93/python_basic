# This one will be named sillycase and it'll take a single string as an argument.
# sillycase should return the same string but the first half should be lowercased 
# and the second half should be uppercased. For example, 

# with the string \"Zakwan\", sillycase would return \"zakWAN\".

def sillycase(string):
    half = round(len(string)/2)
    first_half = string[:half].lower()
    second_half = string[half:].upper()
    return first_half + second_half


sillycase("Zakwan")
