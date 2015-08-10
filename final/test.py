__author__ = 'etkvadi'

def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        print "iteration=", iteration, " L=", L, " lst=", lst
        iteration += 1
    return lst


def sort2(lst):
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions assume this line just executed
        print "iteration=", iteration, " L=", L
    return lst

def sort3(lst):
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions assume this line just executed
        print "iteration=", iteration, " L=", L
    return out

def sort4(lst):
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])

        L = lst[:]  # the next 3 questions assume this line just executed
        print " L=", L
        return unite(front, back)


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here

    tmp = {}
    ret = []
    for k in aDict.keys():
        v = aDict[k]
        tmp[v] = tmp.get(v,0) + 1

    for k in aDict.keys():
        cnt = tmp[aDict[k]]
        if cnt == 1:
            ret.append(k)

    return sorted(ret)


aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print uniqueValues(aDict)

aDict = {1: 1, 2: 1, 3: 1}
print uniqueValues({0: 4, 9: 4, 3: 4, 5: 2, 1: 1})

