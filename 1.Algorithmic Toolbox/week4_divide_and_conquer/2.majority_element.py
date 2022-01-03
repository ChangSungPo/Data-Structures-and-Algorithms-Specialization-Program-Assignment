# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    
    tmp, count  = a[0], 1
    for i in range(1, len(a)):
        if a[i] == tmp:
            count += 1
        elif count > 0:
            count -= 1
        else:   
            tmp = a[i]
            count += 1
    check = 0       
    for i in range(len(a)):
        if (a[i] == tmp):
            check += 1
    if (check > len(a)/2):
        return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [2, 3, 9, 2, 2]
    # n = len(a)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
