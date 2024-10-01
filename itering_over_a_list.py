numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []
even_count = 0
for number in numbers:
    if (number % 2 == 0):
        even_numbers.append(number)
        even_count += 1

print(even_numbers)
print("There are ", even_count, " numbers in the even list.")
print("There are ", len(even_numbers), " numbers in the even list.")

valueList = [5, 3, 8, -1, -2.2, 0]
minValue = valueList[0]

for minor in valueList:
    if (minor < minValue):
        minValue = minor

print(" The min value is ", minValue)

planets = ["Sun", "Mercury", "Venus", "Earth", "Mars"]

for planet in planets:
    if (planet == "Sun"):
        print(planet, "is not a planet")
    else:
        print(planet, "is a planet")

    if (planet == "Mercury"):
        print(planet, "is closet to the Sun")


month = "February"
print(month, "is a spelled:")

for x in month:
    print(x, end = ' ')

name = input("What is your first name?")
print(name, "is spelled:")
letterCount = 0
for x in name:
    print(x)
    letterCount += 1

print(f"{letterCount} letters in the name {name}")

for x in range(10):
    print(x)

for x in range(0, 10):
    print(x)

for x in range(1, 7):
    print(x)

for x in range(0, 30, 7):
    print(x)

for x in range(5, -1, -1):
    print(x)

add_numbers = []
for number in range(1,1201):
    if (number % 2 != 0):
        add_numbers.append(number)

print(add_numbers)