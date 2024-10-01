x = 4
while (x < 125):
    x = 2 * x
    print("x is now: ", x)

inp = input('Hi ! Please say Hello.')
while inp != 'Hello':
    inp = input('Hi ! Please say Hello.')
print('It\'s about time!')

password = ""
while password != 'secret':
    password = input('Please enter the password')
    if password == 'secret':
        print('Welcome')
    else:
        print('Sorry, the password you entered is incorrect. Please try again.')

x = 1
while x <= 10:
    if x == 5:
        break #this will break out the loop immediately
    print(x)
    x += 1

for number in range(1, 21):
    #Test for ad number
    if (number % 2 != 0):
        #Test for multiple of 3
        if (number % 3 == 0):
            continue
        print(number)

#Multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i * j))

num_list = []
i = 0
playing = True
while (playing == True):
    num = int(input('Enter an int : '))
    if (num == -1):
        playing = False
    else:
        num_list.append(num)
        i += 1

num_sum = 0
for num in num_list:
    num_sum += num

num_avg = num_sum / i
print("avg : ", num_avg)

string = 'pasta'
rev = ''
for j in range(len(string) -1, -1, -1):
    rev += string[j]

print(rev)

my_list = [1, 2, 3, 4]
my_list.append(5)
my_list.pop()
my_list.pop(1)
print(my_list)

print('cat' in my_list)

x = 0
for x in range(5):
    if x == 3:
        continue
    print(x)

lst = []
for i in range(2):
    for j in range(1, 3):
        lst.append(i * j)
print(lst)
