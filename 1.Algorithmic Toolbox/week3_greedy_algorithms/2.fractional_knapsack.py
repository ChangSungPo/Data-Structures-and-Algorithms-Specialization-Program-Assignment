# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    per_value = [values[i]/weights[i] for i in range(len(weights))]

    while len(per_value) != 0:
        if (capacity == 0):
            return round(value, 4)        
        to_pick = max(per_value)
        to_pick_index = per_value.index(to_pick)
        del per_value[to_pick_index]
        pick_weight = min(capacity, weights[to_pick_index])
        del weights[to_pick_index]
        capacity = capacity - pick_weight
        value += to_pick*pick_weight


    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = [3,50,60,20,100,50,120,30]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
