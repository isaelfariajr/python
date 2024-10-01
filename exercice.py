# your code here
def getFactors(x):
    """Returns a list of factors of the given number x."""
    factors = []
    for i in range(1, x + 1):
        if (x % i == 0):
            factors.append(i)

    return factors


num = 2
factors_test = [1, 2]
factors = getFactors(num)
print(factors_test, factors, str(factors) + ' are not the factors of ' + str(num))
