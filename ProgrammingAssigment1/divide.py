import sys
ipt = sys.argv[1]
file = open(ipt, 'r')
arry = [int(x.strip()) for x in file.readlines()]


def half_count(arry):
    left = 0
    indice = 0
    if length == 4:
        for i in a[0:-1]:
            for j in a[1:]:
                print('i: ', i)
                print('j: ', j)
                if i > j:
                    if (i <= length) & (j <= length):
                        left = left + 1
                print('left: ', left)
                # elif i > j
                #     if (i > length) & (j > length):
                indice = indice + 1
        print('total count: ', indice)

    return left

def count_inv(left, right):
    inv = 0
    for i in left:
        for j in right:
            if i > j:
                inv = inv + 1
    return inv

def count_total(arry):
    length = len(arry)/2
    print('length: ', length)
    a = arry[0:int(length)]
    print('the array first half is: ', a
    if length <= 4:
        total = half_count(a) + count_inv(a)
    elif length > 4:
        total = count_total(arry)
    return total

print('the array is: ', arry)
print('\nit has this number of inversions: ', left_count(arry))
