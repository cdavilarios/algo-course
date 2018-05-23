import sys
import numpy as np
import time
ipt = sys.argv[1]
file = open(ipt, 'r')
A = [int(x.strip()) for x in file.readlines()]

def partition(A, l, r):
    count = 0
    if (r - l) <= 1:
        count = 0
    else:
        i = l + 1
        for j in range(l + 1, r):
            if A[j] < A[l]:
                A[i], A[j] = A[j], A[i]
                i = i + 1
            j = j + 1
        A[l], A[i - 1] = A[i - 1], A[l]
        print('final array is: ', A)
        count = r - l - 1 + partition(A, l, i - 1) + partition(A, i, r)
    return count


def comparisons(A):
    r = len(A)
    l = 0
    count = partition(A, l, r)
    return count


start_time = time.clock()
print('initial array is: ', A)
print('\nit has this number of comparisons: ', comparisons(A))
print(time.clock() - start_time, 'seconds')
