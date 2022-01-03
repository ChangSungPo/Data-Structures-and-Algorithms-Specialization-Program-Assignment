# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    tmp = [previous, current]

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

        r = sum % 10

        tmp.append(r)

        if (tmp[-2] == 0 and tmp[-1] == 1):
            tmp = tmp[:len(tmp)-2]
            index = n % len(tmp)
            return tmp[index]

    return tmp[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
