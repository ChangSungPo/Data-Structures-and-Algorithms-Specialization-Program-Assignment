# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max = 0
    second_max = 0

    for i in range(n):
        if numbers[i] > max:
            max = numbers[i]

    for j in range(n):
        if numbers[j] > second_max and numbers.index(max) != j:
            second_max = numbers[j]
    


    


    return max*second_max


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
