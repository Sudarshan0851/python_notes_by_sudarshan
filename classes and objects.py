"""what is object oriented programming language?
In python each line of code is a object where it has its own identity, attributes
and methods of interaction based on this object ,belongs to a category known
as class
class --> blueprint of object
object --> instence of class

#The main purpose of classes and object are to avoid duplicates and build a
common codes so every user can use it


IF condition --> decison making codes
for loop --> run instructions over all elements
def --> executes block of code when we call it

ex: Bank --> customers   --> online banking -->
#q)How the OOP's concept will works? baesd on rules
#The rules of Object oriented programming language--> 4 rules or pillers
#1.encapsulation  :-  wrapping the data and methods in a single class
#restrict direct access to some private data
ex:- can we directly change account balance --> No
#2.polymorphism :- one method behave differently based on objects
#3.abstraction :- Hiding the implementation and show necessary features
#4.Inheritence :- one class can inherit properties from another class

#How many types of attributes / properties / data that we want to share?
#there 2 types
#1.class attributes :- common sharable data or properties
#2.object attributes :- unique and non sharable attributes
"""
#create a class customers
class customer():
    #create class attributes
    Bank_name = "Hfc bank"
    IFSC   = "HFC0009876"
    Branch = "Ameerpet"
    City  = "Hyderabad"
    State = "TG"
    """create object attributes
    before creating object attributes, we need to intialise object attributes
    inside the class"""
    def __init__(self,name,account,balance,mobile):
        self.name = name
        self.`account = account
        self.balance = balance
        self.mobile = mobile
    #what is a method?
    #methods are functions created inside the class
    def welcome_wish(self):
        return(f"Hello {self.name},welcome to {self.Bank_name}!")
    def check_balance(self):
        return(f"Hello {self.name},your current balance is  {self.balance}!")
    def deposit(self,amount):
        self.balance += amount
        return(f"""deposite amount is {amount}/-
        the updated balance is {self.balance}/-""")
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            return(f"""withdrawal amount is {amount}/- 
            the updated acc balance is {self.balance}/-""")
        else:
            return(f""" {self.name} , your current balance is {self.balance}/- """)

#create an object
c1 = customer("sai",3743648,15000,988765635)
c2 = customer("java",6263532,10000,827323832)

#access the class attributes
"""print(c1.IFSC)
print(c2.Branch)"""
#access the object attributes
#print(c2.balance)
#access the method
"""print(c1.welcome_wish())
print(c2.check_balance())"""
"""
print(c1.withdraw(30000))
print(c2.deposit(30000))"""
"""
step 1: create a class :- use class
step 2: create a object and assign the class to it --->c1=class()
step 3: define the class attribute and object attribute
step 4: create object attributes ----> initiate object attributesinside the class
step 5: create methods ---> functions inside the class
step 6: access the attributes and apply the methods


"""

#=========================#
#iterators :-breaks the large amount of data into small chunks
#how the iteration can be build
#1. __iter__()
#2. __next__()
l = [1,2,3,4,5,6,7,8,9]
"""for i in l:
    print(i)"""
i = iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


#connecting mysql
#handle jason(pandas)
#genrator
#regular expression
#requst