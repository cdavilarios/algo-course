import sys
import numpy as np
import time
from math import ceil
from math import floor
ipt = sys.argv[1]
file = open(ipt, 'r')
A = [int(x.strip()) for x in file.readlines()]


def swaping(A, l, r, p):
    ## swaps the xth element with the 0th element
    x = l
    if p == 'final':
        x = r - 1
    elif p == 'median':
        x = l + ceil((r - l)/2) - 1
    A[x], A[l] = A[l], A[x]
    return A

def partition(A, l, r, p):
    count = 0
    if (r - l) <= 1:
        count = 0
    else:
        print(A)
        A = swaping(A, l, r, p)
        print(A)
        i = l + 1
        for j in range(l + 1, r):
            if A[j] < A[l]:
                A[i], A[j] = A[j], A[i]
                print(A)
                i = i + 1
            j = j + 1
        A[l], A[i - 1] = A[i - 1], A[l]
        print(A)
        count = r - l - 1 + partition(A, l, i - 1, p) + partition(A, i, r, p)
    return count


def comparisons(A, p):
    r = len(A)
    l = 0
    count = partition(A, l, r, p)
    return count


start_time = time.clock()
# print('initial array is: ', A)
# print('\nwith pivot start has this number of comparisons: ', comparisons(A, 'start'))
# print('\nwith pivot final has this number of comparisons: ', comparisons(A, 'final'))
print('\nwith pivot median has this number of comparisons: ', comparisons(A, 'median'))

# print('array pushing final element: ', pushing(A, 1))
# print('\ncomparisons with pivot 0th element: ', comparisons(A))
print(time.clock() - start_time, 'seconds')
