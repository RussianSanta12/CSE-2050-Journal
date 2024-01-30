# Defining a class
    
# Classes are used to create user defined data structures

#definining instant variables
    self.name = name # instance variable

# Methods like this one that start and end with two underscores are sometimes called the "magic methods" or "dunder methods" (https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/)
# You should not make up your own methods starting and ending with two underscores
    # That's how python sets them apart so you don't actually call your own methods
    # Dunder methods are usually not called explicitly but instead provide some other means of calling them 
        #For example
            #When you add the two numbers using the + operator, the __add__ method will be called

# Built in classes in python define many magic methods. Use dir() function to see the number of magic methods inherited by a class
    #ex: dir(int)

#ints
    # have imag and real components
    #can be added, subtracted, compared, etc

#Operator overlaoding
    # A class can implement certain operations that are invoked by a special syntax
    # This is pythons apporach to perator overloading, allowing classes to define their own behavior with respect to language operators
    # (https://www.geeksforgeeks.org/operator-overloading-in-python/)

#self
    #the first argument of every method is a reference to the current instance of the class
    # Although you must specify "self" explicitly when defining the method, you don't include it when calling the method
    # Python passes it for you automatically

class vector:
    def magnitude


    #abstraction focuses on hiding the internal implementations of a process or method from the user. In this way, the user knows what he is doing but not how long the work is being done. 
    #Abstraction is hiding unnecessary information from user. So, abstraction is a method to hide internal functionalites from user
    