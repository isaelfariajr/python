def get_factors(x):
    """Returns a list of factors of give number x."""
    factors = []
    for i in range(1, x + 1):
        #check if i divide number x evenly
        if (x % i == 0):
            factors.append(i)

    return  factors

print(get_factors(21))