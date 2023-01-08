# Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# List Comprehension
first_col = [row[0] for row in matrix]
print(first_col)

mylist = ['a', 2, True, 'abc', 25.3, 3+5j, ['Hello', 'World']]
print(mylist)

mylist = [1, 2, 6, 0, -5, 55]
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)

mylist = ['a', 'b', 'c']
mylist.append(['d', 'e'])
print(mylist)
mylist.extend(['d', 'e'])
print(mylist)
