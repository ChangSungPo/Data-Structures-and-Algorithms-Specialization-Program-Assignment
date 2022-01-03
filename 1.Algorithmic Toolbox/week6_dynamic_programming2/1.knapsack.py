# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = [[0 for i in range(W+1)] for j in range(len(w)+1)]
    for i in range(len(w)+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                result[i][j] = 0
            elif w[i-1] <= j:
                result[i][j] = max(w[i-1] + result[i-1][j-w[i-1]], result[i-1][j])
            else:
                result[i][j] = result[i-1][j]
    return result[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W, w = 10, [1,4,8]
    print(optimal_weight(W, w))
