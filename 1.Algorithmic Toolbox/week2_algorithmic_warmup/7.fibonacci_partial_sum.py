# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 1

    current = 0
    next  = 1

    tmp = [current, next]
    second = tmp[-1]

    for _ in range(to - 1):
        current, next = next, current + next
        sum += next

        tmp.append(sum % 10)

        if (tmp[-2] == 0 and tmp[-1] == 1):
            tmp = tmp[:len(tmp)-2]
            index = to % len(tmp)
            second = tmp[index]
            break
    
        second = tmp[-1]

    if (to == 0):
        second = tmp[0]
    

    if (from_ == 0):
        first = tmp[0]
    else:
        first = tmp[(from_-1) % len(tmp)]


    if (second < first):
        return second - first + 10
    else:
        return second - first



if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))