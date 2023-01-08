import pprint as pp
# Dictonaries
my_stuff={'key1':'val1', 'key2':'val2', 'key3':123, 4:{'a':'z', 'b':"y"}}
pp.pprint(my_stuff)
print(my_stuff[4]['b'].upper())
my_stuff['key5']=[1, 2, 3]
print(my_stuff)
