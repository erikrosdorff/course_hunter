#uncomment to see code
'''
size_input = input("Enter your house in square feet: ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_meters} square meters is {square_feet} square feet")
'''
#uncomment to see code
'''
user_age = input("Enter your age in years: ")
years = int(user_age)
months = years * 12
dog_years = years * 7
seconds = years * (((60*60)*24)*365)
print(f"You are {years} years old, which is {months} months and {dog_years} in dog years that is over {seconds} seconds!")
'''
#uncomment to see code
'''
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
#uncomment to see code
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
#uncomment to see code
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
'''
def multiply(*args): #allows you to input multiple arguements with *
    print(args)
    total = 1 
    for arg in args:
        total = total * arg
    
    return total

print(multiply(9, 4, 98))
'''
#uncomment to see code
'''
def add (x, y):
    return x + y

nums =[3, 5]
print(add(*nums))
nums_dict = {"x": 15, "y":25}
print(add(x=nums["x"], y=nums["y"]))
print(add(**nums)) #does the same as 86 and 87
'''
'''
def multiply(*args): #allows you to input multiple arguements with *
    print(args)
    total = 1 
    for arg in args:
        total = total * arg
    
    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(*args) #the star allows you to pass in indivitual arguements
    elif operator =="+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="*")) #operator = tells the program to enter into the operator argument
#operator= '*'changed to an asterisc it changes to a tuple
'''
#uncomment to see code
'''
# def arg_ast(**kwargs):
#     print(kwargs)

# arg_ast(name="Billy", Level=2)

# #the following doesn't work because we can't have named arguments
# def named_fun(name, level):
#     print(name, level)

# details = {"name" : "Billy", "level" : 25}
# print("details: ", details) #prints entire dictionary
# named_fun(**details) #assigns the associated values from the dictionary 

# def named_fun1(**kwards):
#     print(kwards)

# named_fun1(**details)

# def print_nicely(**kwargs):
#     named_fun1(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(name="billy", age=25)

def both(*args, **kwargs):
    print("args:", args)
    print("kwargs: ", kwargs)

both(9, 0, 8, name="My name")
both(test="itworked")
'''
#uncomment to see code
'''
student = {"name": "Rolf", "grades": (89, 99, 95, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)


class Student:
    def __init__(self): #method when a function is in a class it is called a method
        self.name = "Rolf"
        self.grades = (89, 99, 95, 78, 90)
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student_var = Student()
print(student_var.name, student_var.grades, Student.average(student))
#print("Average:", average(student.grades)) // not needed with classes
'''
class Student:
    def __init__(self, name, grades):
        self.name = name #creates an input that is needed to call #"Rolf" #creates a name property and stores the value "Rolf" into it
        self.grades = grades#(90, 90, 93, 78, 90)
    
    def average_grades(self): #must take a parameter which will be the object (self) created intitially
        return sum(self.grades) / len(self.grades)

#//
# #print("Student(): ", Student()) #prints Student():  <__main__.Student object at 0x0000015FF9D30490>
# student = Student() #calls student class and as it is blank it will call the __init__ method automatically
# name_paramter = Student("Bob", (78, 90 , 80, 95, 99))
# print("student.name: ", student.name) #student.name:  Rolf
# print("student = Student() print(Student()): ", Student()) #student = Student() print(Student()):  <__main__.Student object at 0x0000015FF9D301F0>
# print("student.grades: ", student.grades)
# print("Student.average(average):", Student.average(student))
# #print("student.average(): ", student.average(), "Should be the same as above")
# print("name_paramter.name:", name_paramter.name)
#//

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (90, 96, 87, 99, 100))
print("student.average_grades()", student.average_grades())
print("student2.average_grades():", student2.average_grades())

'''
class Person: #Capitol letters for classes
    def __init__(self, name, age): #initial 
        self.name = name
        self.age = age
'''
