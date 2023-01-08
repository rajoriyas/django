try:
    file = open('simple.txt', 'w')
    file.write("I'm appending my text file")
#except IOError:
except:
    print('Unable to operate file')
else:
    print('Successfully completed operation!')
    file.close()
finally:
    print('Program ends!')
