def myfunc(param='default'):
    """
    this is doc string
    """
    print('i luv myfunc with {} parameter'.format(param))
myfunc()

def add(p1, p2):
    return p1+p2
print(add('1', '2'), type(add('1', '2')))

mylist = [1,2,3,4,5,6,7,8]
# Lambda Expression
print(list(filter(lambda num:num%2==0, mylist)))

# Filter
def even_bool(num):
    return num%2 == 0
print(list(filter(even_bool, mylist)))

# Built-in function
mystr = 'hello world #tweet'
mystr.upper()
mystr.lower()
mystr.capitalize()
mystr.split()

print('x' in [1,2,3,4])
