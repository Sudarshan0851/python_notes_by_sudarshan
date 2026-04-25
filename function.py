#what we need to do when we dont know how many parameters we need to create?

"""def details(**name):
    print(name)

details(name="shahul",age=29,gender="male")"""

#what we need to do when we dont know how many arguments needs to pass?
#print  the summ of given numbers

"""def languages(*name):
    print(name)
languages("python","java","c++")"""


"""
** --> KWARGS --> Keyword arbitrary arguments 
   --> when we dont know how many parameter we need to create use KWARGS
   --> The default data type is Dictionary
*  --> ARGS --> Arbitrary arguments
   --> when we dont know how many arguments we need to pass use ARGS
   --> The default data type for ARGS is Tuple
"""


#write a function that takes any number and returns their sum
#10,20,30 --> 60
"""def total(*num):
    print(sum(num))

total(10,20,30)
"""
#create a function so it can accept the marks and student details
"""def report(*marks,**name):
    print(marks)
    print(name)

report(80,90,95,name="jhon",grade="A")"""
#Return :- it is used to sendback the values to the caller
#when we use the return call the function with print
def sum(x,y):
    return x+y
print(sum(10,20))

#create a function to find the square of a number
#create a function to find the maximum of 2 numbers
#create a function to print the numbers from 1 to N
#CREATE a function to count the characters in a string
#create a function to check the +ve,-ve and neutral 
#create a function to find the largets of 3 numbers 

#List comprehension
#lambda function
#map
#filter