stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below

pos_x = stdform.index('x')
pos_pow = stdform.index('^')
eform = ""
eform = eform + stdform[:pos_x] + 'E'
eform = eform + stdform[pos_x+3 : pos_pow]
eform = eform + stdform[pos_pow+1:]
print("This number in E notation is", eform + ".")
