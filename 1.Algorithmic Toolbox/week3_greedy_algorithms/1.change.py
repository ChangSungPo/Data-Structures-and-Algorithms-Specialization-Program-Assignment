# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = 0
    coin_list = [10,5,1]
    for coin in coin_list:
        if (m < coin):
            continue
        coins += int(m / coin)
        m = m % coin


    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = int(input())
    print(get_change(m))
