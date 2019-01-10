# Question. 1 create a function named first_4 that returns the first four items 
# 		  from whatever iterable is given to it.


def first_4(iterable):
    return iterable[0:4]



# Question 2. Make a new function named first_and_last_4. 
# 			It'll accept a single iterable but, this time, 
# 			it'll return the first four and last four items as a single value.

def first_and_last_4(iterable):
    return iterable[:4] + iterable[-4:]



# Question 3. create a new function named odds that returns every item 
# 			with an odd index in a provided iterable. 
# 			For example, it would return the items at index 1, 3, and so on.

def odd(iterable):
	return iterable[1::2]


# Question 4. Make a function named reverse_evens that accepts a single iterable
# 		 as an argument. Return every item in the iterable with an even index.
# 		 ..in reverse.

# 		For example, with [1, 2, 3, 4, 5] as the input, 
# 		the function would return [5, 3, 1].

def reverse_evens(arg):
    return arg[::2][::-1]
    	

first_4([1,2,6,4,8])