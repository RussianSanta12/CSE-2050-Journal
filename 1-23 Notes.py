# string "str"
# strings in python can be enclosed in single or double quotes
# str1 = "foo bar", str1 = 'foo bar'

#string operations
# str.upper()
# str.lower()

#tuple


# collections methods
#iterate
for i in myList:
    print(i)

for (key,value) in myDict.items():
    print(key,value)

# sequences (str, tuple, list)
myString = "Spamalot"
myString[3]
#myString[1:3] <--- includes "myString[1], but not [3]"

# Functions
    # program redundancy can be reduced by creating a grouping of predefined statements for repeateadly used operations
    # function definition ---> new functions name, list of parameters (optional), and a block of indented statements
       
       # def cook_pizza(type):
            #do stuff here
            #Eventually, return a value:

# Basics and Syntax
    # a function may return one value using a return statement

# def double(x)
    # y = (2**x)
    # return x,y

    # a function can only return one item, not two or more (though a list or a tuple with multiple elements can be returned)

# a parameter is a function input specified in a function definition
    #example: def double(x)

def get_letter_grade(num_grade):
    num_grade=()

    calc_calories(x)
    x = 21

# a variable or function object is only visible to part of a program known as the objects scope
# variable defined inside a function --> scope of that variable is limited to the function
# total_inches and centimeters are visible to the code outside the function
# variable defined inside a function is called a local variable

# variable and function scope
#     variables defined outside of a function are called global variables
#         scope: assignment ---> end of the file
#         can be accessed inside functions

# Function Scope
    # extends from function definition to the end of the file
    # as same as variable, to be able to call a function, it must be already defined
employee_name= 'N/A'

get_name()
print('employee name:', employee_name)

def get_name():
# this wont work as it is in the wrong order!!!!!


#a NAMESPACE is a set of names currently availible to us
    # it maps names to objects
        # when we define a variable it is added to our namespace
        #functions get their own namespace
        # see the current namespace with dir()
    dir()


# scope ---> area of code where name is visible
    #"at least" three nested scopes are active at any point in programs execution
        # 1. Global Scope --> contains all globally defined names outside of function
        # 2. Local scope --> usually refers to names defoined within the current function
            # --> same as global if NO functions are defined
        #3. Built-in Scope ---> contains built-in names of Python. e.g int(), str(), etc.
    # When a name is referenced, Python checks the name space in the following order:
        # Local Scope ---> Global Scope ---> Built-in scope
        # If not found --> NameError
    
    
