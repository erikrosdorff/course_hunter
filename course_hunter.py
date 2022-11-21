'''
size_input = input("Enter your house in square feet: ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_meters} square meters is {square_feet} square feet")
'''
'''
user_age = input("Enter your age in years: ")
years = int(user_age)
months = years * 12
dog_years = years * 7
seconds = years * (((60*60)*24)*365)
print(f"You are {years} years old, which is {months} months and {dog_years} in dog years that is over {seconds} seconds!")
'''
''''
#can add and modify elements to list not tuple
list = ["This", "is", "a", "list"]
list.append("This is appended")
list.append("Remove this item")
list.remove(list[-1])
tuple =("This", "is", "a", "tuple")
#no duplicates no subscript notation
set = {"This", "is", "a", "set"}
set.add("Added element")
print(f"This is the first item in the list: {list[0]}",
f"This is the second item in the tuple: {tuple[1]}.")
print(list, tuple, set)

lambda 

'''
'''
friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

local_friends = friends.difference(abroad) #calls the difference function in the friends variable // only Rolf
print("friends.difference(abroad)", local_friends) #prints rolf

local_friends1 = abroad.difference(friends)
print("local_friends1", local_friends1) #prints empty set

union_friends = abroad.union(friends)
print("union_friends", union_friends)
'''
'''
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    return total / count
'''
def multiply(*args): #allows you to input multiple arguements with *
    print(args)
    total = 1 
    for arg in args:
        total = total * arg
    
    return total

print(multiply(9, 4, 98))
