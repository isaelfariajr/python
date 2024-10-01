def uniq_list(l):
    """Return a list of unit values from given list l"""
    x = []
    for a in l:
        if a not in x:
            x.append(a)

    return x

print(uniq_list([1,2,3,3,3,3,3,4,5]))
