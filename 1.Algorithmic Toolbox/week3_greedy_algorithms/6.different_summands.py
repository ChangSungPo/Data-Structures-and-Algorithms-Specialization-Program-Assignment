# Uses python3
import sys

def optimal_summands(n):
    result = n
    summands = []
    current = 1
    sum = 0
    while True:
        tmp = n-current
        if tmp > current or tmp == 0:
            summands.append(current)
            n -= current
            sum += current
            if sum == result:
                break
        current += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n=10**9
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
