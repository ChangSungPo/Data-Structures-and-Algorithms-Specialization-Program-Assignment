# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    phone_book = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            phone_book[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if phone_book.__contains__(cur_query.number):
                del phone_book[cur_query.number]
        else:
            if phone_book.__contains__(cur_query.number):
                result.append(phone_book[cur_query.number])
            else:
                result.append("not found")
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

