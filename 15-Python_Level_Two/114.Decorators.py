s = 'Global Varriable'

def func():
    mylocals = 'Local Varriable'
    print(locals())
    print(globals())
    print(globals()['s'])

    global s
    s = 50
    print(s)

func()

def hello(name):
    return 'Hello '+name

print(hello('Rahul'))
greet = hello
print(greet('Rahul'))

"""
def hey(name='Rahul'):
    print('Hey')
    def greet():
        return 'Greet'
    def welcome():
        return 'Welcome'
    print(greet())
    print(welcome())
hey()
"""

def hey(name='Rahul'):
    print('Hey')
    def greet():
        return 'Greet'
    def welcome():
        return 'Welcome'
    if name == 'Rahul':
        #return greet
        return greet()
    else:
        #return welcome
        return welcome()
#x = hey
#print(x())

x = hey()
print(x)

def greet():
    return 'Greet'
def other(func):
    return func()+' Rahul'
print(other(greet))

print('\n')

# Decorator
def new_decorator(func):
    def wrap_func():
        print('Code before execution')
        func()
        print('Code after execution')
    return wrap_func

def func_needs_decorator():
    print('Function')

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

print('\n')

def new_decorator(func):
    def wrap_func():
        print('Code before execution')
        func()
        print('Code after execution')
    return wrap_func
    
@new_decorator
def func_needs_decorator():
    print('Function')

#func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
