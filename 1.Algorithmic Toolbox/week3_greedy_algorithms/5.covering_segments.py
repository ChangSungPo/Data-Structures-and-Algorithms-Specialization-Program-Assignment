# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    while True:
        max_start = max(segments, key=lambda x:x.start).start
        points.append(max_start)
        segments = list(filter(lambda x: x.end < max_start, segments))
        if not segments:
            break
    
    #write your code here

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # segments = [Segment(4,7), Segment(1,3), Segment(2,5), Segment(5,6)]
    points = optimal_points(segments)
    points.sort()
    print(len(points))
    print(*points)
