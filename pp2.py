#PYTHON SYNTAX


"""Insert the missing part of the code below to output "Hello World"."""
print("Hello, World")

"""Complete the code block, print "YES" if 5 is larger than 2.
 Hint: remember the indentation."""
if 5 > 2:
    print("YES")

#PYTHON COMMENTS


"""Comments in Python are written with a special character, which one?"""
#This is a comment

#Use a multiline string to make the a multiline comment:#
"""This is a comment
written in 
more than just one line"""


#PYTHON VARIABLES

'''Create a variable named carname and assign the value Volvo to it.'''
carname = "Volvo"

'''Create a variable named x and assign the value 50 to it.'''
x=50

'''Display the sum of 5 + 10, using two variables: x and y.'''
x=5
y=10
print(x+y)

'''Create a variable called z, assign x + y to it, and display the result.'''
x = 5
y = 10
z = x + y
print(z)

'''Insert the correct syntax to assign values to multiple variables in one line:'''
x,y,z= "Orange", "Banana", "Cherry"

'''Insert the correct syntax to assign the same value to all three variables in one code line.'''
x = y = z = "Orange"

'''Insert the correct keyword to make the variable x belong to the global scope.'''
def myfunc():
  global x
  x = "fantastic"



#PYTHON DATA TYPES

'''The following code example would print the data type of x, what data type would that be?'''
x = 5
print(type(x))
#int

'''The following code example would print the data type of x, what data type would that be?'''
x = "Hello World"
print(type(x))
#str

'''The following code example would print the data type of x, what data type would that be?'''
x = 20.5
print(type(x))
#float

'''The following code example would print the data type of x, what data type would that be?'''
x = ["apple", "banana", "cherry"]
print(type(x))
#list

'''The following code example would print the data type of x, what data type would that be?'''
x = ("apple", "banana", "cherry")
print(type(x))
#tuple

'''The following code example would print the data type of x, what data type would that be?'''
x = {"name" : "John", "age" : 36}
print(type(x))
#dict

'''The following code example would print the data type of x, what data type would that be?'''
x = True
print(type(x))
#bool



#PYTHON NUMBERS

'''Insert the correct syntax to convert x into a floating point number.'''
x = 5
x = float(x)

'''Insert the correct syntax to convert x into a integer.'''
x = 5.5
x = int(x)

'''Insert the correct syntax to convert x into a complex number.'''
x = 5
x = complex(x)

#PYTHON STRINGS

'''Use the len function to print the length of the string.'''
x = "Hello World"
print(len(x))

'''Get the first character of the string txt.'''
txt = "Hello World"
x = txt[0]

'''Get the characters from index 2 to index 4 (llo).'''
txt = "Hello World"
x = txt[2:5]

'''Return the string without any whitespace at the beginning or the end.'''
txt = " Hello World "
x = txt.strip()

'''Convert the value of txt to upper case.'''
txt = "Hello World"
txt = txt.upper()

'''Convert the value of txt to lower case.'''
txt = "Hello World"
txt = txt.lower()

'''Replace the character H with a J.'''
txt = "Hello World"
txt = txt.replace('H','J')

'''Replace the character H with a J.'''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))



