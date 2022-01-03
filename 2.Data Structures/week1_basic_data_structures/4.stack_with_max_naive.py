#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_number = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.max_number) == 0:
            self.max_number.append(a)
        elif a >= self.max_number[-1]:
            self.max_number.append(a)

    def Pop(self):
        assert(len(self.__stack))
        tmp = self.__stack.pop()
        if len(self.max_number):
            if self.max_number[-1] == tmp:
                self.max_number.pop()

    def Max(self):
        assert(len(self.__stack))
        # return max(self.__stack)
        return self.max_number[-1]

    


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        # query = [["push", 1],["push", 2],["max"],["pop"],["max"]]

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
