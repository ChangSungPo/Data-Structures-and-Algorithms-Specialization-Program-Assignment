# Uses python3
import sys

def optimal_sequence(n):
    min_step = [0]
    result = [[1]]
    for i in range(1, n + 1):
        min_step.append(10**100)
        tmp1, tmp2, tmp3 = 10**100, 10**100, 10**100
        if i >= 2:
            if i%2 == 0 and i//2 != 0:
                tmp1 = min_step[(i-1)//2] + 1
            if i%3 == 0 and i//3 != 0:
                tmp2 = min_step[(i-1)//3] + 1
            tmp3 = min_step[i-1-1] + 1
            tmp = min(tmp1, tmp2, tmp3)
            if (tmp == tmp1):
                result_part = result[(i-1)//2].copy()
                result_part.append(result_part[-1]*2)
            elif (tmp == tmp2):
                result_part = result[(i-1)//3].copy()
                result_part.append(result_part[-1]*3)
            else:
                result_part = result[-1].copy()
                result_part.append(result_part[-1]+1)
            min_step[i-1] = tmp
            result.append(result_part)
    return result[-1]

input = sys.stdin.read()
# input = 1
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
