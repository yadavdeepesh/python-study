# import sys
import random
# print("Hello, World! ")
# print(sys.version)


# if 5>3:
#     print("5 is greater than 3") 
# if 5 > 2:
#         print("Five is greater than two!")    

# if 5 > 2:
 #indentation error
#  print("Five is greater than two!")
#      print("Five is greater than two!") 

#create a variable

x = 5
y = "Hello, World!"
# print(x)

# create a comment in python

# this is a comment

# print("Hello, World!") # this is a comment
# print("Have a nice day!") # this is a comment
# print("Learning Python is fun!") # this is a comment

# Semicolons (Optional, Rarely Used)

# Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read:

# print("Hello"); print("World") # this is a comment

# if 5 > 2:
#  print("Five is greater than two!")

# if 5 > 2:
#  print("Five is greater than two!") 

# x = 5
# y= "Hello, World!"
# print(x)
# print(y)


# print("Hello World!")
# print("Have a good day.")
# print("Learning Python is fun!")

# print("Hello"); print("How are you?"); print("Bye bye!")

# print("Hello, World!") # this is a comment
# print("Have a good day!") # this is a comment
# print("Learning Python is fun!") # this is a comment

# print("Hello World!", end=" ")

# print("I will print on the same line.")

# print use with numbers

# print(5)
# print(358)

# print(2+6)
# print(5*3)
# print(10/2)
    
# You can combine text and numbers in one output by separating them with a comma:

# print("The sum of 5 and 10 is", 5 + 10)
# print("I am deepesh ",28, "year old")

# print("I am",25 ,"years old.")

#This is a comment
# print("Hello, World!")

# """
# This is a comment
# written in
# more than just one line
# """
# print("Hello, World!")

# create a variable and assign a value to it
# x= 5
# y= "Hello, World!"
# print(x)  
# print(y)  

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

# If you want to specify the data type of a variable, this can be done with casting.
# x= str(3)
# y= int(3)
# z= float(3)
# print(x)
# print(y)
# print(z)    

# You can get the data type of a variable with the type() function.

# x = 5
# y = "Hello, World!"

# print(type(x))
# print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

# x = "John"

# print(x)

# y = 'John'
# print(y)

# Case-Sensitive
# Variable names are case-sensitive.
# a= 4
# A= "Sally"
# print(a)
# print(A)

# Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# MyVar = "John"      
# myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Remember that variable names are case-sensitive



# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariabkeName = "John"

# Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"
# FirstName = "John"

# Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"
# my_favorite_color = "Green"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

# x, y, z = "Orange", "Banana", "Cherry"

# print(x)
# print(y)
# print(z)    

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)    

# Unpack a Collection

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Output Variables
# The print() function is often used to output variables.

# x = "Python is awesome"
# print(x)

# In the print() function, you output multiple variables, separated by a comma:

# x = "Python"  
# y = "is"  
# z = "awesome"  
# print(x, y, z)  

# You can also use the + operator to output multiple variables:

# print(x + y + z)  

# For numbers, the + character works as a mathematical operator:

# x = 5
# y = 10
# print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# x = 5
# y = "John"
# print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
# print(x, y)

# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside of a function, and use it inside the function

# x = "awesome"

# def myfunc():
#   print("Python is " + x)
# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)


# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# Example
# If you use the global keyword, the variable belongs to the global scope:

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)



# x = 5
# y="deepesh"

# print(type(x))
# print(type(y))

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# x = "Hello World" # str
# print(type(x))
# x = 20 # int
# print(type(x))      
# x = 20.5 # float
# print(type(x))
# x = 1j # complex            
# print(type(x))                              
# x = ["apple", "banana", "cherry"] # list
# print(type(x))
# x = ("apple", "banana", "cherry") # tuple
# print(type(x))
# x = range(6) # range
# print(type(x))
# x = {"name" : "John", "age" : 36} # dict
# print(type(x))
# x = {"apple", "banana", "cherry"} # set
# print(type(x))                                  
# x = frozenset({"apple", "banana", "cherry"}) # frozenset
# print(type(x))
# x = True # bool
# print(type(x))
# x = b"Hello" # bytes
# print(type(x))
# x = bytearray(5) # bytearray
# print(type(x))
# x = memoryview(bytes(5)) # memoryview       
# print(type(x))
# x = None # NoneType
# print(type(x))


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# x = str("Hello World") # str
# print(type(x))
# x = int(20) # int
# print(type(x))
# x = float(20.5) # float
# print(type(x))
# x = complex(1j) # complex           
# print(type(x))  
# x= list(("apple", "banana", "cherry")) # list
# print(type(x))
# x = tuple(("apple", "banana", "cherry")) # tuple
# print(type(x))
# x = range(6) # range
# print(type(x))
# x = dict(name="John", age=36) # dict
# print(type(x))
# x = set(("apple", "banana", "cherry")) # set
# print(type(x))
# x = frozenset(("apple", "banana", "cherry")) # frozenset
# print(type(x))
# x = bool(5) # bool
# print(type(x))
# x = bytes(5) # bytes
# print(type(x))
# x = bytearray(5) # bytearray
# print(type(x))
# x = memoryview(bytes(5)) # memoryview
# print(type(x))  

# challenege

# x = 5
# print(type(x))
# y = 3.345
# print(type(y))
# z ="Deepesh"
# print(type(z))    


# Python Numbers
# There are three numeric types in Python:

# int
# float
# complex

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex  

# print(type(x))
# print(type(y))
# print(type(z))

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# x = 1
# y = 35656222554887711
# z = -3255522            
# print(type(x))
# print(type(y))
# print(type(z))


# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# x = 1.10
# y = 1.0     
# z = -35.59
# print(type(x))
# print(type(y))                  
# print(type(z))

# Complex
# Complex numbers are written with a "j" as the imaginary part:

# x = 3+5j
# y = 5j
# z = -5j
# print(type(x))
# print(type(y))              
# print(type(z))

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

# Example
# Convert from one type to another:

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex          

# a = float(x) # convert from int to float
# b = int(y)   # convert from float to int
# c = complex(x) # convert from int to complex

# print(a)
# print(b)
# print(c)    

# print(type(a))
# print(type(b))                          
# print(type(c))

# Note: You cannot convert complex numbers into another number type.

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# examples

# import the random module, and display a random number between 1 and 9:


# print(random.randrange(1, 10))

# x = 5
# y = 3.14
# z = 2+3j
# print(type(x))
# print(type(y))
# print(type(z))


"""
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""

# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3  

# print(x)
# print(y)
# print(z)    

# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")
# print(x)
# print(y)
# print(z)
# print(w)

# x = str("s1")
# y = str(2)
# z = str(3.0)
# print(x)
# print(y)
# print(z)

# Challenge: Casting
# Test your understanding of Python type casting by completing a small coding challenge.

# x = 1

# a = float(x) # convert from int to float
# print(a)

# b = str(x)   # convert from int to str
# print(b)    

# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:

# print("Hello")
# print('Hello')

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

# print("It's alright.")
# print('He said "Hello"')    
# print("He said 'Hello'")

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

# a = "Hello"
# print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

# a = "Hello, World!"
# print(a[1])

# looping in string

# for x in "banana":
#   print(x)

# // String Length
# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

# b = "Hello, World!"
# print(b[2:5])

# Note: The first character has index 0.

# Slice From the Start
# By leaving out the start index, the range will start at the first character:

# b = "Hello, World!"
# print(b[:5])
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:

# a = "Hello, World!"
# print(a.replace("l", "J"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

# a = "Hello"
# b = "World" 
# c = a + b
# print(c)

# Example
# To add a space between them, add a " ":

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# age = 36
# txt  = f"my name is Deepesh, and I am {age} years old."
# print(txt)

# place holders

# price = 49
# txt = f"The price is {price} dollars."
# print(txt)


# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# Example
# Display the price with 2 decimals:

# price = 59
# txt = f"The price is {price:.2} dollars"
# print(txt)

# Example
# Perform a math operation in the placeholder, and return the result:

# txt = f"The price is {20 * 59} dollars"
# print(txt)


txt = "Hello, World!"
print(txt[2:5])

print(txt.upper())

name = "Deepesh"
age = 28
txt = f"My name is {name}, and I am {age} years old."
print(txt)








