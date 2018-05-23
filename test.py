    x = 0
    if p == 'final':
        x = r - 1
    elif p == 'median':
        x = ceil(r/2) - 1

def pushing(A, x):
    ## take the x_th element of the array "A" and inserts it at the 0th element
    ## removing it from its position
    A.insert(0, A[x])
    A.pop(x+1)
    return A

A = pushing(A, x)
print('A after pushing xth element: ', A)
#
 print('\ncomparisons with pivot 0th element: ', comparisons(A, 'start'))
