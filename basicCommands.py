print("Hello World !")
print('Hello World in sinngle quotes !')
print('today', 'is a good day')
print('Good morning', end = ' ')
print('Brandon')
print('Good night', 'Brandon', sep = ', ')
print(2+3)
print(5-6)
print(2*3)
print(3+5-2*6)
print((3+5-2)*6)
print(type(99))
print(type(1.3))
print(type(23.0))
print(type(-5.1))
print(type(2*3.5))
print(type(7/2.0))
print(type(0.1))

print(3/2)
print(3.1/2)
print(3//2)
print(3.1//2)
print(3%2)
print(4%2)
print(3.1%2)

print(1 == 2)
print(1 < 2)
print(1.2 < 1.2)
print('Car' == 'Car')
print('Car' == 'car')
print('Car' == 'car')
print('1' == 1)
print('1' != 1)
print(bool(False))
print(bool(True))
print(bool(7))
print(bool(0))
print(bool(7 ==0))
print(bool(5000 % 2 ==0))
print(bool(5003 % 2 >= 1))

print('Nice !')
print("Nice !")
print("Nice !" == 'Nice !')
print('Wow !' + ' Python is so cool')
print(type('Wow !' + ' Python is so cool'))
print(type('103'))
print(type(103))
print('Name:', 'Brandon', 'Krakowsky')
print('Name: ' + 'Brandon ' + 'Krakowsky')
print('Brandon\'s last name is Krakowsky')

print(12374/621)
print(int(12374/621))
print(round(12374/621))
print(int('1'))
print(4/2)
print('4 % 2 = ', 4 % 2)
print('4 % 2 = ' + str(4 % 2))
print('Is 4 even ? ', str(4 % 2 == 0))

fav_movie = input("What is your favorite movie ?")
fav_singer = input("What is your favorite singer ?")
favs = "Your favorite move is {} and your favorite singer is {}".format(fav_movie, fav_singer)
print(favs)