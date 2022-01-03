# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)

    while True:
        if (left == right):
            return -1

        mid = (right - left)//2

        if (a[mid+left] == x):
            return mid+left

        if (a[mid+left] > x):
            right = mid + left
        else:
            left = mid + 1 + left
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

    # a = [1,5,8,12,13]
    # target = [8,1,23,1,11]

    # a=[1,2,3,4,5]
    # target=[1,2,3,4,5]

    # for x in target:
    #     print(binary_search(a, x))
