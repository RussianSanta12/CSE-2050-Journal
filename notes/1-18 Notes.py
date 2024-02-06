# single line comments start with #

#integer 'int'
#float 'float'

#boolean
# a boolean expression is one that is either true or false
# True and false are special values that belong to the type bool; they are not strings
# to compare two values, we use relational operator

#operators
#operators are special symbols that represent computations like addition and multiplication
#the values the operator is applied to are called operands
#The operators +,-,*, / and ** perform addition, subtraction, multiplication, division, and exponentation. 
print(5**2)
#this will print "25"

#sets
# a set is an unordered collection with no duplicate elements
#unordered: set doesn't matter the order
# heterogeneous: set can contain data of all types
# unique: set doesn't allow duplicate items
# ex: 
S = {20, 'Jessa', 35.75}
print(S)

#set operations
#add(): adds an element to the set
#clear(): removes all elements from the set
#difference(): returns a set containing the difference between two or more sets
#remove(): removes the specified element; raises an error when the element doesn't exist
#discard(): remove the specified item; doesn't raise error if the element is not present in the set
#pop(): removes an element from the set

#Dictionary
#unordered collections of unique values stored in (key-value) pairs
#unique: keys should be unique
#mutable: we can add/modify/remove key values after the creation
__dict__ = {'a':10,'b':20,'c':30}
print(__dict__)

#dictionary operations
#clear(): removes all the elements
#copy: returns a copy of the dictionary
#get(): returns the value of the specified key



