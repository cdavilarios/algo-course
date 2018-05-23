import sys
import numpy as np
import time
from math import ceil
ipt = sys.argv[1]
file = open(ipt, 'r')
A = [int(x.strip()) for x in file.readlines()]


def partition(A, l):
    # print('A as its reading is: ', A)
    # print('l is:', l)
    r = len(A)
    count = 0
    if r <= 1:
        count = 0
    else:
        i = 0
        for j in range(0, r):
            # print('A[j]: ', A[j])
            # print('r is: ', r)
            # print('l is:', l)
            # print('A[l]: ', A[l])
            if A[j] < A[l]:
                A[i], A[j] = A[j], A[i]
                # print('A array is: ', A)
                i = i + 1
            j = j + 1
        A[l], A[i] = A[i], A[l]
        print('A array is: ', A)
        count = r - 1 + partition(A[0:i], i - 1) + partition(A[i + 1: r], r - i - 2)
    return count


def comparisons(A):
    ## by default pivot takes the first element of the array
    r = len(A)
    l = r - 1
    count = partition(A, l)
    print(A)
    return count



start_time = time.clock()
print('initial array is: ', A)
print('\ncomparisons with pivot 0th element: ', comparisons(A))
print(time.clock() - start_time, 'seconds')
