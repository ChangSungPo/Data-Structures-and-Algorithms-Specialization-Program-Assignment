# Uses python3
import sys

def lcm_naive(a, b):
    intput_a, input_b = a, b
    while True:
        if (a == 0):
            tmp = b
            break
        if (b == 0):
            tmp =  a
            break

        
        if a >= b:
            a, b = b, a%b
        else:
            a, b = a, b%a

    result = intput_a*input_b/tmp


    return int(result)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

