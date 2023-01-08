x = 20
def my_func():
    x = 50
    return 50
print(x)
print(my_func())

# Local Scope
lambda x:x**2

# Emclosing Local Scope
name = 'rajoriyas'
def greet():
    name = 'rahul'
    def hello():
        print('hello', name)
    hello()
greet()

# Built in Scope
len_ = 23
print(len_)

# Global Function
x = 120
def myFunc():
    global x
    x = 20
myFunc()
print(x)
