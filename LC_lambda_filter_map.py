"""list comprehension:it offers a smaller codes when a new list
is created form the existing list

syntax --->[item for item in collection <condition>]
"""


"""fruit = ["apple", "banana", "cherry","mango","orange"]
new=[]
for i in fruit:
    if "e" in i:
        new.append(i)

print(new)
"""

l2 = ["java","orange","apple","python"]
def check(l):
    new =[]
    for i in l:
        if "e" in i:
            new.append(i)

    print(new)


check(l2)

#list comprehension --->[item for item in coll <condition>]
new2 = [i for i in l2 if "e" in i]
print (new2)

#create range of even odd number from 0 to 100 and store in new list
l3 = [23,34,43,5,4,565]
new3 = [i for i in l3 if i%2==0]
print(new3)
print(new3)

new4 = [item for item in range (101) if item%2==1 ]
print(new4)

"""lambda function  : is an anonymous function where it 
takes many arguments and single expression

syntax ---> lambda arguments : single expression

lambda is powerfull when we use inside the
another  function so functions are first class objects """

a= lambda x,y : x+y
print(a(10,53))
print(a)

#arguments : when we call a function we pass a values known as arguments
#expression : steps or measures used to give a output to user is known as expression

"""
map(): it takes a function as an argument and 
run over each element in the collection

syntax ---> map 
"""


"""for i in age:
    if age >= 18:
        print("true")
    else:
        print("false")"""
age =  [23,32,4,12,13,23,35,3,12,12,43,19,18]
def check_age(age):
    if age >= 18:
        return("eligible")
    else:
        return("noteligible")
# map(function, collection)

# m1= list(map(check_age,age))
# print(m1)

m = tuple(map(lambda x : x%2==0, age))
print(m)

l2  = ["python","java","c","c++"]
#write a code of list comprehension that prints the length of each element in the list and store in a new list
new = [len(i) for i in l2]
print(new)

#solve it using a map functuion
m = list(map (len, l2))
print(m)

""" filter function :- it takes functions as an arguments
 and print the data which is condition true    
 syntax ---> filter(fun, coll)
 
 """
"""age = [10,19,19,4,11,44,32,43,45,66,55]

f = list(filter(lambda x : x>=18, age))
print(f)
"""
#take a list of number and return the containing list of each numbers square 1,4,6,9
l1 = [1,4,6,9]
f1 = list(filter(lambda x:x>=2 ,l1))
print(f1)
#convert all names into a uppercase by using map function jhon abhi basheer charan
names = ["jhon", "abhi", "basheer", "charan"]

upper_names = list(map(str.upper, names))

print(upper_names)

#from the given numbers filter only even numbers 10 , 15 ,20,25,30,35
num = [10,15,20,25,30]
f1=list (filter (lambda x : x%2==0, num))
print(f1)
#filter the words which are longer than 4 character cat , elephant , dog , tiger , lion
animal=["cat",'elephant','dpg','tiger','lion']
f2 = list(filter(lambda x : len(x)>=4, animal))
print(f2)
#convert the celisus to fahrenheit using map formula is f = (c * 9/5)+32'
cel = [1,2,3,4,5,5,67,3]
ma = list (map (lambda x : (x * 9/5)+32,cel))
print(ma)





