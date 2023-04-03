# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class phoneNumber:
    size = 100
    multiplier = 66
    prime = 29

    def __init__(self):
        self.buckets = [0] * self.size

    def _hash_func(self, s):
        hashed = (s * self.multiplier) % self.prime
        return hashed % self.size
    
    def add(self, number, name):
        hashed = self._hash_func(number)
        self.buckets[hashed] = name

    def delete(self, number):
        hashed = self._hash_func(number)
        self.buckets[hashed] = 0

    def find(self, number):
        hashed = self._hash_func(number)
        if self.buckets[hashed] == 0:
            return 'not found'
        return self.buckets[hashed]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = phoneNumber()
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            contacts.delete(cur_query.number)
        else:
            result.append(contacts.find(cur_query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
