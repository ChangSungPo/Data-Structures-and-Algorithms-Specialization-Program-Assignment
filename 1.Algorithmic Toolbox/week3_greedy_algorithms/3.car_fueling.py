# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    cur, count = 0, 0
    if (tank >= distance):
        return 0
    stops.insert(0, cur)
    
    while cur < len(stops):
        prev = cur
        while cur < len(stops):
            if (cur != len(stops)-1):
                if (stops[cur+1]-stops[prev] <= tank):
                    cur += 1
                else:
                    break
            else:
                break
        
        if (prev == cur):
            return -1
        
        if (cur < len(stops)):
            count += 1
        
        if (distance - stops[cur] <= tank):
            return count

    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d, m, _, stops = 950,400,4,[200,375,550,750]
    # d, m, _, stops = 10,3,4,[1,2,5,9]
    # d, m, _, stops = 1100,400,4, [100,300,500,700,800]
    # d, m, _, stops = 100,400,4, [10,30,40,80]
    print(compute_min_refills(d, m, stops))
