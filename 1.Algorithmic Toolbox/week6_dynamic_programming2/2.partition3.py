# Uses python3
import sys
import itertools
import numpy

def partition3(A):
    total_weight = sum(A)
    if len(A) < 3:
        return 0
    if total_weight%3 != 0:
        return 0
    
    W = total_weight//3
    n = len(A)
    items = A
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: 
                count += 1
    # print(value)
    if count < 3: 
        return 0
    else: 
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # A = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    # A = [3,3,3]
    print(partition3(A))

