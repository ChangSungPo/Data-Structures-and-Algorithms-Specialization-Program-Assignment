# Uses python3
import sys

def get_change(m):
    #write your code here
    coin_list = [1,3,4]
    min_num_coins = [0]
    for i in range(1, m + 1):
        min_num_coins.append(10**100)
        for coin in coin_list:
            if i >= coin:
                tmp =  min_num_coins[i-coin] + 1
                if tmp < min_num_coins[i]:
                    min_num_coins[i] = tmp
    return min_num_coins[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    # m = 34
    # print(get_change(m))
