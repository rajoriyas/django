def func():
    print('Func() in one.py')

print('Top level of one.py')

if __name__ == '__main__':
    print('one.py is running directly')
else:
    print('one.py is imported')
