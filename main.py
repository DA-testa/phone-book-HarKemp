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
        self.buckets = [[] for i in range(100)]

    def _hash_func(self, s):
        hashed = (s * self.multiplier) % self.prime
        return hashed % self.size
    
    def add(self, number, name):
        hashed = self._hash_func(number)
        bucket = self.buckets[hashed]
        if name not in bucket:
            self.buckets[hashed] = [name] + bucket

    def delete(self, number):
        hashed = self._hash_func(number)
        for i in range(len(self.buckets)):
            if i == hashed:
                self.buckets[i] = 0
                break

    def find(self, number):
        hashed = self._hash_func(number)
        if self.buckets[hashed] != 0:
            my_string = ' '.join(self.buckets[hashed])
            return my_string
        return "not found"


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
