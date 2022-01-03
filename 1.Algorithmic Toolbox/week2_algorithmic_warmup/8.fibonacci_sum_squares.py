# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    tmp = [previous, current]

    for _ in range(n):
        previous, current = current, previous + current
        tmp.append(current % 10)
        
        if (tmp[-2] == 0 and tmp[-1] == 1):
            tmp = tmp[:len(tmp)-2]
            break

    return (tmp[n%len(tmp)]*tmp[(n+1)%len(tmp)]) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    # n = int(input())
    print(fibonacci_sum_squares_naive(n))
