def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

a = 2
b = 3
result = greater_than(a, b)
print("{} is great then {} : {}".format(a, b, result))