import sys
import numpy as np
import time
ipt = sys.argv[1]
file = open(ipt, 'r')
arry = [int(x.strip()) for x in file.readlines()]


def half_count(arry):
    indice = 0
    if len(arry) == 1:
        indice == 0
    else:
        if (arry[0] > arry[1]):
            indice = indice + 1
    return indice

def count_inv(left, right):
    inv = 0
    for i in left:
        for j in right:
            if i > j:
                inv = inv + 1
            j = j + 1
        i = i + 1
    return inv

def count_total(arry):
    length = np.ceil(len(arry)/2)
    left = arry[0:int(length)]
    right = arry[int(length):]
    if length <= 2:
        total = half_count(left) + half_count(right) + count_inv(left, right)
    else:
        total = count_total(left) + count_total(right) + count_inv(left, right)
    return total


start_time = time.clock()
print('\nit has this number of inversions: ', count_total(arry))
print(time.clock() - start_time, 'seconds')
