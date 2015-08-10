__author__ = 'vanja'

# exponential complexity

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] # list of empty list
    # get all subsets without last element
    smaller = genSubsets(L[:-1])
    # create a list of just last element
    extra = L[-1:]
    new = []
    # for all smaller solutions add one with last element
    for small in smaller:
        new.append(small + extra)
    #combine those with last element and those without
    return smaller+new


print genSubsets([1,2])