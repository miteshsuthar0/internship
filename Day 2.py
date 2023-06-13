import gtts

# Dictionaries in Python
import functools

import self as self

# --creating dictionaries

myDictionary = {"key-1": "Value-1", "key-2": "Value-2", "key-3": "Value-3", "key-4": "Value-4"}

print(myDictionary)
print(myDictionary['key-2'])

IntegerDict = {10: "C++", 20: "Java", 30: "Python", 40: "Ruby"}

print(IntegerDict[30])

Cars = {"Maruti_Suzuki": "Swift, Ciaz, ""celerio,", "Tata": "Tiago, Tigor, Punch, ""Nexon, ""Harrier, Safari"}
print(Cars)
print()
print(Cars['Tata'])
print()
emptylist = {}

emptylist["India"] = "Delhi", "Gujrat", "Rajasthan"
emptylist["Gujrat"] = "Ahmedabad", "Gandhinagar", "Kutch"

print(emptylist)
print()
print(emptylist['Gujrat'])
print()
# ---Accesing elements from Dictionary

for i in Cars:
    print("Key : " + i + "  || Elements : " + Cars[i]);

print()
del emptylist['Gujrat']  # To delete a key and its values
print(emptylist)
print()
emptylist['Gujrat'] = "Ahmedabad, ""Kutch"  # Appending key-value in Dictionary
print(emptylist)

Cars.update(emptylist)  # to update dictionary - Adding two different dictionaries
print(Cars)

print()

# --Functions of Dictionaries

print("Length of the Cars Dictionary is : " + str(len(Cars)))  # To print length of dictionary
print()
emptylist.clear()  # to clear Any Dictionary
print("This is an Empty Dictionary : " + str(emptylist))

print(Cars.values())  # To Access all values from Drictionary
print()
print(Cars.keys())  # To Access all keys from Drictionary
print()
print(Cars.items())  # To Access all items from Drictionary
print()

print(Cars.__contains__('Tata'))  # To check if any key contains in the dictionary or not
print(Cars.__contains__('Mahindra'))

# --Tuples

myTuple = 1, 2, 3, 4  # Creating Tuple
print(myTuple)

secondTuple = 5, 6, "Seven", 8
print(secondTuple)

# --Adding element to Tuple


Fruits = "Apple", "Orange", "Banana", "Berry ", "Mango"
print(Fruits[2])  # accessing element of tuple using index
Fruits = Fruits + ("Grapes",)  # Adding Element to tuple
print(Fruits)

IntegerTuple = (1, 2, 3, 4) + (5, 6, 7, 8)  # Adding two tuples
print(IntegerTuple)

# -- Deleting Tuple


del (IntegerTuple);  # To Delete any Tuple

# print(IntegerTuple)                       gives error that ItegerTuple is not Defined

# -- Slicing Tuple

x = (1, 2, 3, 4, 5)
print(x[1:4])

# -- Basic Operations and Function of Tuple

a = (1, 2)
print(a * 4)  # multiplication of tuple

a = (1, 2, 6) + (4, 5) + (3,)  # Addition
print(a)

b = 4 in a  # using in keyword
print(b)

print(len(a))  # to print length of tuple

print(max(a))  # prints max value that tuple contains
print(min(a))  # prints minimum value that tuple contains

# -- Relational Operators

print(5 < 9)
print(5 <= 9)
print(5 == 9)
print(5 != 9)
print(5 > 9)
print(5 >= 9)

print("abc" < "aaa")
print("abc" > "aaa")
print("aaa" == "aaa")
print("aaa" == "aab")
print("aaa" != "aaa")

# -- Logical Operators

print(True and False)
print(5 < 7 and 7 > 6)

print(not False)
print(not 5 > 3)

print(True or False)
print(5 > 2 or 5 > 8)

# print()
# x = int(input("enter a number : "))
#
# print(x>1 and x<100)


# -- Conditional Statements

# Available_balance = 1000
# WithdrawAmount = int(input("Enter amount you want to withdraw : "))
# if Available_balance < WithdrawAmount :
#     print("Insufficient Balance ! ")
# else:
#     Available_balance = Available_balance - WithdrawAmount
#     print("Available Balance : " + str(Available_balance))


# -- elif

# Morning: 0600 to 1159
# Noon: 1200
# Afternoon: 1201 to 1700
# Evening: 1701 to 2000
# Night: 2000 to 0559

# time = int(input("Enter time without : sign -- "))

# if time>=600 and time<1159:
#     print("Morning")
# elif time == 1200:
#     print("Noon")
# elif time>=1201 and time<1700:
#     print("AfterNoon")
# elif time>=1700 and time<2000:
#     print("Evening")
# elif ((time>=2000) and (time<2400) or (time>=0) and (time<=559)):
#     print("Night")
# else:
#     print("Invalid entry!")
#
# -- nested if

#
# if time>=600 and time<1159:
#     print("Morning")
# else:
#     if time == 1200:
#         print("Noon")
#     else:
#         if time>=1201 and time<1700:
#             print("AfterNoon")
#         else:
#             if time>=1700 and time<2000:
#                 print("Evening")
#             else:
#                 if ((time>=2000) and (time<2400) or (time>=0) and (time<=559)):
#                     print("Night")
#                 else:
#                     print("Invalid entry!")


# n = int(input())
#
# if n % 2 == 0:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n >= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n >= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Weird")


# Looping
#
# list = [1, 2, 3, 4, 5, 6, 78, 9]
#
# for i in range(0, len(list)):
#     print(list[i])

# for i in range(0, 7, 2):
#     print(i)

# bigList = [[1, 3, 6], [8, 2, ], [0, 4, 7, 10], [1, 5, 2], [6]]

# for i in bigList:
#     for j in i:
#         print(" Element of list within list : ",j)
#

# i = 0
# while i < 5:
# 	i=i+1
# 	print ("i =", i)

#
# bigList = [[1, 3, 6], [8, 2,], [0, 4, 7, 10], [1, 5, 2], [6]]
# i = 0
# j = 0
# while i<len(bigList):
# 	while j<len(bigList[i]):
# 		print ("Element of list within a list -",bigList[i][j])
# 		j=j+1;
# 	i=i+1

name = "Mitesh"


# for i in name:
# 	if not i.islower():
# 		continue
# 	print (i)

# for i in name:
# 	if i == "t":
# 		break;
# 	print (i)


# -- Practice Question

# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).


# for i in range(1500, 2701):
#     if (i % 7 == 0 and i % 5 == 0):
#         print(i)
#

#  2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

# temp = input("Enter Temprature you want to covert : ")
# degree = int(temp[:-1])
# temp_convention = temp[-1]
#
# if temp_convention == "f" or temp_convention == "F":
#     temp_in_celsius = (degree-32)*(5/9)
#     print("Temprature in Celsius is : " + str(temp_in_celsius) + "C")
#
# elif temp_convention == "c" or temp_convention == "C":
#     temp_in_fahrenheit = (degree*(9/5)+32)
#     print("Temprature in Fahrenheit is : " + str(temp_in_fahrenheit) + "F")


# 3. Write a Python program to guess a number between 1 and 9.

# number = 6
# for i in range(10):
#     guess_number = int(input("Enter any number : "))
#     if guess_number == number:
#         print("Well Guessed")
#         break
#     else:
#         print("Wrong Guess.Try Again ! ")


# 4. Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# n = 5
# for i in range(n):
#     for j in range(i):
#         print("* ",end="")
#     print(" ")
# #
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print("")
# #

# 5. Write a Python program that accepts a word from the user and reverses it.
#
# word = input("Enter a word that you want to reverse :  ")
# print(word[::-1])


# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

# numbers = (1,2,3,4,5,6,7,8,9)
# odd = []
# even = []
#
# for i in range(len(numbers)):
#     if (i%2==0):
#         even.append(i)
#     elif (i%2==1):
#         odd.append(i)
#
# print("Number of even Numbers : " + str(len(even)))
# print("Number of odd Numbers : " + str(len(odd)))

# 7. Write a Python program that prints each item and its corresponding type from the following list.


# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
#
# for i in datalist:
#     print(str(i) + " " + str(type(i)))

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
#
# for i in range(6):
#     if (i == 3 or i == 6):
#         continue
#     else:
#         print(i, end= " ")

# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
#
# first = 0
# second = 1
# next_int = None
#
# print(str(first) + " " + str(second), end=" ")
#
# # for i in range(9):
# #     next_int = first + second
# #     first = second
# #     second = next_int
# #     print(str(next_int), end=" ")
#
# while True:
#     next_int = first + second
#     if next_int < 50:
#         print(next_int, end=" ")
#         first = second
#         second = next_int
#     else:
#         break

# 10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number
# and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

#
# for i in range(50):
#     if (i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif (i%3==0):
#         print("Fizz")
#     elif (i%5==0):
#         print("Buzz")
#     else:
#         print(i)


# 11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
#
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
#
# m_Row = int(input("Enter Value of rows you want : "))
# n_Columns = int(input("Enter Value of columns you want : "))
# multi_list = [[0 for col in range(n_Columns)] for row in range(m_Row)]
# multi_list = []
#
# for i in range(m_Row):
#     for j in range(n_Columns):
#         multi_list.append(0)
#
# for i in range(m_Row):
#     for j in range(n_Columns):
#         multi_list[i][j] = i*j
#
# print(multi_list)
#


# 13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input.
# The program will print the numbers that are divisible by 5 in a comma separated sequence.
# Sample_Data = 0100,0011,1010,1001,1100,1001
# Expected Output : 1010


# ---List Compreension-------


# cars = ["jaguar", "tata", "tesla","ford"]
# new_cars = [x if x != "tesla" else "Audi" for x in cars]
# new_cars = []

# for x in cars:
#     if x != "tesla":
#         new_cars.append(x)
#     else:
#         new_cars.append("Audi")

# print(new_cars)


# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).


# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         print(f"My name is {self.name}")
#
#     # def show(self):
#     #     print(f"My Name is {self.name}")
#
#
# p = Person('Mitesh')
# print(p)


# class Vehicle:
#     pass
# p1 = Vehicle(120,20.4)
#
# print(p1.max_speed)
# print(p1.mileage)

# class Addition:
#     def __init__(self, f, s):
#         self.first = f
#         self.second = s
#
#     def display(self):
#         print("First number is : " + str(self.first))
#         print("Second number is : " + str(self.second))
#         print("Addition is : " + str(self.answer))
#
#     def calculate(self):
#         self.answer = self.first + self.second
#
# p1 = Addition(234,786)
#
# p2 = Addition(12,78)
#
# p1.calculate()
# p2.calculate()
#
# p1.display()
# p2.display()

# class myClass:
#     def __init__(self,name=None):
#         if name is None:
#             print("Default constructor called.")
#         else:
#             self.name = name
#             print("constructor called with name :", self.name)
#
#     def method(self):
#         if hasattr(self,'name'):
#             print("method called with name :", self.name)
#         else:
#             print("method called without name.")
#
# p1 = myClass()
# p2 = myClass('Mitesh')
#
# p1.method()
# p2.method()

# generaotor function with yield keyword

# def inf_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# for i in inf_sequence():
#     print(i, end=" ")


# ---   Fibonacci using Generator Function

# def Fib(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
#
# x = Fib(15)
#
# for i in Fib(50):
#     print(i)


# -------Single Inheritance-------
# Subclassing (Calling constructor of parent class)

# class Person(object):
#     def __init__(self, name, ID):
#         self.name = name
#         self.id = ID
#
#     def Display(self):
#         print("Name :",self.name)
#         print("Id :",self.id)
#
# class Employee(Person):
#     def __init__(self,name, id, salary, post):
#         self.sal = salary
#         self.post = post
#
#         Person.__init__(self, name, id)
#
#     def Display(self):
#         print("Name :",self.name)
#         print("ID : ",self.id)
#         print("Salary :",self.sal)
#         print("Post :",self.post)
#
#
# a = Employee('Mitesh', 'Pata nahi dete hi nai h', 'kuch nai milta puchhke dukhti nass mat daba', 'itna sb padhke pata nai chala k INTERN hu !')
#
# a.Display()


# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def Display(self):
#         print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self,name,age,n,a):
#         self.Name = n
#         self.Age = a
#
#         super().__init__(name,age)
#
#     def DisplayInfo(self):
#         print(self.Name,self.Age)
#
# a = Student('Mitesh',20,'UmedSingh',19)
#
# a.Display()
# a.DisplayInfo()


# Adding properties

# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def Display(self):
#         print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self,name,age,n,a,dob):
#         self.Name = n
#         self.Age = a
#         self.dob = dob
#
#         super().__init__(name,age)
#
#     def DisplayInfo(self):
#         print(self.Name,self.Age,self.dob)
#
# a = Student('Mitesh',20,'UmedSingh',20,'25-03-2003')
#
# a.Display()
# a.DisplayInfo()

# # ------------Multiple inheritances------------
#
# class Base1():
#     def __init__(self):
#         self.x = "jay"
#         print("Base1")
#
# class Base2():
#     def __init__(self):
#         self.y = "Shree Ram"
#         print("Base2")
#
# class Derived(Base1, Base2):
#     def __init__(self):
#
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
#
#     def DisplayData(self):
#         print(self.x,self.y)
#
# a = Derived()
# print(Derived.mro())
#
# a.DisplayData()


# -------------Hierarchical inheritance---------

# class Base():
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         print(self.name,self.age)
#
# class Derived1(Base):
#     def __init__(self,name,age,dob):
#         self.dob = dob
#
#         Base.__init__(self,name,age)
#
#     def Display1(self):
#         print(self.name,self.age,self.dob)
#
# class Derived2(Base):
#     def __init__(self, name, age, dob,resident):
#         self.res = resident
#
#         Base.__init__(self, name, age)
#
#     def Display2(self):
#         print(self.name, self.age,self.res)
#
#
# a = Derived2("Mitesh",20,"04-07-2003","Ahmedabad")
# b = Derived1("Mitesh",20,"04-07-2003")
# b.Display1()
# a.Display2()


# ------------Multilevel inheritance-------------

#
# class Base():
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         print(self.name,self.age)
#
# class child(Base):
#     def __init__(self,name,age,dob):
#         self.dob = dob
#
#         Base.__init__(self,name,age)
#
#     def Display1(self):
#         print(self.name,self.age,self.dob)
#
# class Grandchild(child):
#     def __init__(self, name, age, dob, resident):
#         self.res = resident
#
#         child.__init__(self, name, age,dob)
#
#     def Display2(self):
#         print(self.name, self.age,self.res,self.dob)
#
#
# a = Grandchild("Mitesh",20,"04-07-2003","Ahmedabad")
# b = child("Mitesh",20,"04-07-2003")
# b.Display1()
# a.Display2()


#
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     @classmethod
#     def get_name(cls, name):
#         return cls(name)
#
#
#
# @staticmethod
#
#
# def get_value(self, name="zxc"):
#     return self.value
#
#
# # Create an instance of MyClass
# obj = MyClass(10)
# obj1 = MyClass.get_name('Mitesh')
#
# # Call the get_value method on the instance
# print(obj.value)  # Output: 10
# print(obj1.value)


# Question:
# You are given a list of integers. Write a Python function called square_numbers that takes in a list of integers as input and returns a new list containing the squares of the input numbers.
#
# Your task is to implement the square_numbers function using the map() function to solve the problem.
#
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]


# l = [1,3,5,2,7]
#
# result = map(lambda a:a*a,l)
# print(list(result))

#Question:
# You are given a list of numbers.
# Write a Python function called product_list that takes in a list of numbers as input and returns the product of all the numbers in the list.
# Your task is to implement the product_list function using the reduce() function from the functools module to solve the problem.
#
# Note: You will need to import the reduce() function from the functools module.
#
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: 120 (1 * 2 * 3 * 4 * 5)

from functools import reduce

# def product_list(numbers):
#     # Use reduce() function to multiply all numbers
#     # Return the final product

# Test the function
# input_numbers = [1, 2, 3, 4, 5]
# print(product_list(input_numbers))
# result = functools.reduce(lambda a,b:a*b,input_numbers)

# print(result)

# Question:
# You are given a list of numbers.
# Write a Python function called even_numbers that takes in a list of numbers as input and returns a new list containing only the even numbers from the input list.
#
# Your task is to implement the even_numbers function using the filter() function to solve the problem.
#
# Example:
# Input_numbers =  [1, 2, 3, 4, 5]
# Output: [2, 4] (only the even numbers from the input list)

# even_list = filter(lambda a:a%2==0,Input_numbers)
# print(list(even_list))









#------------Simple Banking System------------

# class BankAccount():
#
#
#     def __init__(self, account_number,balance = 0.0):
#         self.ac = account_number
#         self.balance = balance
#
#     def deposit(self,deposit_amount):
#         self.depo_amt = deposit_amount
#         self.balance = self.balance + self.depo_amt
#
#     def withdraw(self,withdraw_amount):
#         self.with_amt = withdraw_amount
#         self.balance = self.balance - self.with_amt
#
#     def get_balance(self):
#         balance = self.balance
#         return balance
#
# account = BankAccount("123456789")
#
# account.deposit(500)
#
# account.withdraw(200)
#
# balance = account.get_balance()
#
# print("Current balance :",balance)
#

# -------text to speech-------

# text = input(" Enter : ")
#
# txt = gtts.gTTS(text,lang="en")
#
# txt.save("voice.mp3")