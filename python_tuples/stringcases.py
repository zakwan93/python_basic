# Challange : Create a function named stringcases that takes a single string 
# but returns a tuple of different string formats. The formats should be:
# All uppercase
# All lowercase
# Titlecased (first letter of each word is capitalized)
# Reversed
# There are str methods for all but the last one.

def stringcases(string):
    return (string.upper(), string.lower(), string.title(), string[::-1])


# Challange. Create a function named combo that takes two ordered iterables. 
# These could be tuples, lists, strings, whatever.
# Your function should return a list of tuples. Each tuple should hold the first item
# n each iterable, then the second set, then the third, and so on. 
# Assume the iterables will be the same length.
# Check the code below for an example.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(itr1, itr2):
    output = []
    for i in range(0,len(itr1)):
        output += (itr1[i], itr2[i]),
    return output