# python3

from collections import namedtuple
import collections

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = collections.deque(maxlen=size)

    def process(self, request):
        # write your code here
        if not self.finish_time:
            self.finish_time.append(request[0] + request[1])
            return Response(False, request[0])
        else:
            while len(self.finish_time) > 0:
                if self.finish_time[0] <= request.arrived_at:
                    self.finish_time.popleft()
                else:
                    break
            # self.finish_time = [x for x in self.finish_time if x > request[0]]
            # self.finish_time = list(filter(lambda x: x > request[0], self.finish_time))
            if not self.finish_time:
                self.finish_time.append(request[0] + request[1])
                return Response(False, request[0])
            else:
                if (len(self.finish_time) < self.size):
                    last_finish_time = self.finish_time[-1]
                    new_finish_time = last_finish_time + request[1]
                    self.finish_time.append(new_finish_time)
                    return Response(False, last_finish_time)
                return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
