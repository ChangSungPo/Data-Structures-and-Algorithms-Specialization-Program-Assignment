# python3

def ShiftDown(i, n, data, swaps):
    minIndex = i
    l = 2*i+1
    if l < n and data[l] < data[minIndex]:
        minIndex = l
    r = 2*i+2
    if r < n and data[r] < data[minIndex]:
        minIndex = r
    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        swaps.append((i,minIndex))
        ShiftDown(minIndex, n, data, swaps)
    return data, swaps

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    for i in range(n//2-1, -1, -1):
        data, swaps = ShiftDown(i, n, data, swaps)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n


    # data = [5,4,3,2,1]
    # data.reverse()


    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
