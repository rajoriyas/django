# Strings
# Basics
mystring='abcdefg'

# Indexing
print(mystring[-2])

# Slicing
"""Boundary has not included."""
print(mystring[2:5])
print(mystring[:-2])
print(mystring[::2])    # step size

# Basic Method
print(mystring.upper())
print(list(mystring))
mystring="Hello World"
print(mystring.split())

# Print Formatting
x = "Item one: {} Item Two: {}".format('dog', 'cat')
print(x)
x = "Item one: {b} Item Two: {a}".format(a='dog', b='cat')
print(x)
