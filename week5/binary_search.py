__author__ = 'vanja'

def search(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = low + int((high - low) / 2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)


def swapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L



def modSwapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L


L1 = []
L3 = [4,3,54,221,235,8,322,43,2]

swapSort(L1)
modSwapSort(L1)

L2 = [4,3,2,1]
swapSort(L2)
L2 = [4,3,2,1]
modSwapSort(L2)

swapSort(L3)
modSwapSort(L3)