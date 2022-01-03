# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    tmp = []

    tmp.append(0)
    tmp.append(1)

    for _ in range(n - 1):
        previous, current = current, previous + current
        tmp.append(current%m)
        if (previous%m == 0 and current%m == 1):
            tmp = tmp[0:len(tmp) - 2]
            reminder = n%len(tmp)
            return tmp[reminder]
    
    return tmp[-1]

if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
