# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count

        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        hash_value = self._hash_func(query.s) if query.type != "check" else query.ind
        if query.type == "check":
            chain = ""
            if self.elems.__contains__(hash_value):
                if len(self.elems[hash_value]) != 0:
                    chain = self.elems[hash_value]
            self.write_chain(chain)
        else:
            if query.type == 'find':
                if self.elems.__contains__(hash_value):
                    self.write_search_result(True if query.s in self.elems[hash_value] else False)
                else:
                    self.write_search_result(False)
            elif query.type == 'add':
                if self.elems.__contains__(hash_value):
                    if query.s not in self.elems[hash_value]:
                        self.elems[hash_value].insert(0, query.s)
                else:
                    self.elems[hash_value] = [query.s]
            else:
                if self.elems.__contains__(hash_value):
                    if query.s in self.elems[hash_value]:
                        self.elems[hash_value].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
