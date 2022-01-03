# Uses python3
import sys

def gcd_naive(a, b):

    while True:
        if (a == 0):
            return b
        if (b == 0):
            return a

        
        if a >= b:
            a, b = b, a%b
        else:
            a, b = a, b%a
        

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
