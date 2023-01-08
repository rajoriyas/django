import one
print('Top level of two.py')
one.func()
if __name__ == '__main__':
    #main()
    print('Two.py is running directly')
else:
    print('Two.py is imported')
