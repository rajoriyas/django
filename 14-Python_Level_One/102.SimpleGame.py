###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
digits = digits[:3]
print(digits)

# Another hint:
repeat = 1
hints = list()
while repeat == 1:
    guess = [int(i) for i in list(input("What is your guess? "))]
    for i in range(3):
        if guess[i] == digits[i]:
            hints.append('Match')
        elif guess[i] in digits:
        #elif all(digit in guess for digit in digits):
            hints.append('Clone')
        else:
            hints.append('Nope')
    print('Your hints:')
    for hint in hints:
        print(hint)
    if hints.count('Match') == 3:
        print('Correct Guess!')
        repeat = 0
    hints.clear()

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
