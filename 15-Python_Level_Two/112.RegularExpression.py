import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not with other'
for pattern in patterns:
    print("I'm searching fot pattern", pattern)
    match = re.search(pattern, text)
    if match:
        print('Match! at position:', match.start())
    else:
        print('No Match!')

split_term = '@'
email = 'user@gmail.com'
print(re.split(split_term, email))

print(re.findall('r', 'rajoriya.rahul04@gmail.com'))

def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print('Searching for pattern', pattern)
        print(re.findall(pattern, phrase))
        print('\n')
test_phrase = 'sdsd..sssddd..sdddsddd..dsds..dssssss..sddddd'
# sd* -> after 's', 'd' comes in range 0 to infinite
# sd+ -> after 's', 'd' comes in range 1 to infinite
# sd? -> after 's', 'd' comes in range 0 and 1
# s[sd] -> after 's', 'sd' comes in range 1 to infinite
test_pattern=['sd*', 'sd+', 'sd?', 'sd{3}', 'sd{1,3}', 'sd{1,3}s', 's[sd]+']
multi_re_find(test_pattern, test_phrase)

# Exclude
test_pattern = ['[^!.?]+']
test_phrase = 'This is string! but with punctuation. How can we remove it?'
multi_re_find(test_pattern, test_phrase)

# Lower Case
test_pattern = ['[a-z]+', '[A-Z]+']
test_phrase = 'This is string! but with punctuation. How can we remove it?'
multi_re_find(test_pattern, test_phrase)

# Numbers
test_pattern = [r'\d+']
test_phrase = 'This is string! but with numbers 123221. How can we filter them?'
multi_re_find(test_pattern, test_phrase)

# Non numeric
test_pattern = [r'\D+']
test_phrase = 'This is string! but with numbers 123221. How can we filter them?'
multi_re_find(test_pattern, test_phrase)

# White Space
test_pattern = [r'\s+']
test_phrase = 'This is string! but with numbers 123221. How can we filter them?'
multi_re_find(test_pattern, test_phrase)

# Non white space
test_pattern = [r'\S+']
test_phrase = 'This is string! but with numbers 123221. How can we filter them?'
multi_re_find(test_pattern, test_phrase)

# Alpha numeric
test_pattern = [r'\w+']
test_phrase = 'This is string! but with symbol #hashtage. How can we filter them?'
multi_re_find(test_pattern, test_phrase)

# Non Alpha Numeric
test_pattern = [r'\W+']
test_phrase = 'This is string! but with symbol #hashtage. How can we filter them?'
multi_re_find(test_pattern, test_phrase)
