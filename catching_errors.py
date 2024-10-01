number = input('Please input an integer.')
try:
    number = int(number)
except ValueError as e:
    print('Your input is not an integer')
    print(e)
else:
    print(str(number)  + ' is indeed an integer')