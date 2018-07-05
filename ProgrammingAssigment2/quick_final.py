import sys
import numpy as np
import time
from math import ceil
from math import floor
ipt = sys.argv[1]
file = open(ipt, 'r')
arry = [int(x.strip()) for x in file.readlines()]


def middle(arry, start, length):
    a = len(arry[start:length])
    if a % 2 != 0:
        m_value = int(a//2)
    elif a == 1:
        m_value = 0
    else:
        m_value = int(a/2 - 1)
    return m_value

def swaping(arry, start, length, pivot):
    ## swaps the xth element with the 0th element
    swap = start
    if pivot == 'final':
        swap = length - 1
    elif pivot == 'median':
        m_value = middle(arry, start, length)
        # print('start value is: ', start)
        # print('end value is: ', length - 1)
        # print('middle value is: ', m_value)
        swap = arry.index(np.median([arry[start], arry[start + m_value], arry[length - 1]]))
        # print('swap median value position is: ', swap)
    arry[swap], arry[start] = arry[start], arry[swap]
    return arry

def partition(arry, start, length, pivot):
    count = 0
    if (length - start) <= 1:
        count = 0
    else:
        # print(arry)
        arry = swaping(arry, start, length, pivot)
        # print(arry)
        i = start + 1
        for j in range(start + 1, length):
            if arry[j] < arry[start]:
                arry[i], arry[j] = arry[j], arry[i]
                # print(arry)
                i = i + 1
            j = j + 1
        arry[start], arry[i - 1] = arry[i - 1], arry[start]
        # print(arry)
        count = length - start - 1 + partition(arry, start, i - 1, pivot) + partition(arry, i, length, pivot)
    return count


def comparisons(arry, pivot):
    length = len(arry)
    start = 0
    count = partition(arry, start, length, pivot)
    return count


start_time = time.clock()
# print('initial array is: ', arry)
# print('\nwith pivot start has this number of comparisons: ', comparisons(arry, 'start'))
# print('\nwith pivot final has this number of comparisons: ', comparisons(arry, 'final'))
print('\nwith pivot median has this number of comparisons: ', comparisons(arry, 'median'))

# print('array pushing final element: ', pushing(arry, 1))
# print('\ncomparisons with pivot 0th element: ', comparisons(arry))
print(time.clock() - start_time, 'seconds')
