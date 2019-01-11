# write a function named covers that accepts a single parameter, a set of topics. 
# Have the function return a list of courses from COURSES 
# where the supplied set and the course's value (also a set) overlap.

# For example, covers({"Python"}) would return ["Python Basics"].

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(courses):
	answer = []
	for key,value in COURSES.items():
		if value.intersections(courses):
			answer.append(key)
	return answer


# Create a new function named covers_all that takes a single set as an argument. 
# Return the names of all of the courses, in a list, where all of the topics 
# in the supplied set are covered.

# For example, covers_all({"conditions", "input"}) would return 
# ["Python Basics", "Ruby Basics"]. Java Basics and PHP Basics would be excluded 
# because they don't include both of those topics.



def covers_all(topics):
    answer = []
    for course,value in COURSES.items():
        if (value & topics) == topics:
            answer.append(course)
        
    return answer





