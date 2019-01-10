
teachers  = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
			 'Kenneth Love': ['Python Basics', 'Python Collections']}

def num_teachers(test2):
    return len(test2)

# 2. Create a new function named num_courses that will receive the 
# same dictionary as its only argument.
# The function should return the total number of courses for all of the teachers.
    
def num_courses(teachers):
    return sum(len(v) for v in teachers.values())


# 3. make another new function named courses that will, again, 
# take the dictionary of teachers and courses.

# courses, though, should return a single list of all of the available 
# courses in the dictionary. No teachers, just course names!

def courses(teachers):
    output = []
    for value in teachers:
        output.extend(teachers[value])
    return output 

# 4. Create a function named most_courses that takes our good ol' teacher dictionary.
# most_courses should return the name of the teacher with the most courses. 
# You might need to hold onto some sort of max count variable.

