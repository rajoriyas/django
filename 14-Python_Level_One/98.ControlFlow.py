# If-else Control Statement
if not print('1'):
    print(print('2'))
else:
    print('3')

if 1 < 2:
    print(True)

# For Loops
seq = list(range(1, 11, 1))
for item in seq:
    print(item, end=' ')
print('\n')

dict = {'key1':'val1', 'key2':'val2', 'key3':'val3'}
for key in dict:
    print(key, ':', dict[key])
print('\n')

for key, val in dict.items():
    print(key, ":", val)
print('\n')

for key, val in enumerate(dict):
    print(key, ":", val)

mypair = [(1,2), (3,4), (5,6)]
for (tuple1, tuple2) in mypair:
    print(tuple1)
    print(tuple2)

# While Loop
i = 0
while i < 5:
    print('i is {}'.format(i))
    i += 1

# List Comprehension
item = list(range(1,5))
out = [i**2 for i in item]
print(out)
