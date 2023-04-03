# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
        elif self.type == 'find':
            self.name = None

class phoneNumber:
    size = 100
    multiplier = 66
    prime = 29

    def __init__(self):
        self.buckets = [[] for _ in range(self.size)]

    def _hash_func(self, number):
        hashed = (number * self.multiplier) % self.prime
        return hashed % self.size
    
    def add(self, number, name):
        hashed = self._hash_func(number)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == number:
                bucket[i] = (number, name)
                break
        else:
            self.buckets[hashed].append((number, name))

    def delete(self, number):
        hashed = self._hash_func(number)
        bucket = self.buckets[hashed]
        for item in bucket:
            if item[0] == number:
                bucket.remove(item)
                break

    def find(self, number):
        hashed = self._hash_func(number)
        for item in self.buckets[hashed]:
            if item[0] == number:
                return item[1]
        return 'not found'


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = phoneNumber()
    for query in queries:
        if query.type == 'add':
            contacts.add(query.number, query.name)
        elif query.type == 'del':
            contacts.delete(query.number)
        else:
            result.append(contacts.find(query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
