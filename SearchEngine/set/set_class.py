
class Set(object):

    def __init__(self):
        self.table = [[] for i in range(50)]
        self.n = 0

    def __str__(self):
        a=""
        for e in self.table:
            a += str(e) + "\n"
        return a


    def add(self, key):
        hash_key = hash(key) % len(self.table)
        key_exists = False
        bucket = self.table[hash_key]
        for i, k in enumerate(bucket):
            if key == k:
                key_exists = True
                break
        if not key_exists:
            bucket.append(key)
            self.n += 1

    def search(self, key):
        hash_key = hash(key) % len(self.table)
        bucket = self.table[hash_key]
        for k in bucket:
            if key == k:
                return k

    def __or__(self, other):
        result = Set()
        for e in self.table:
            for k in e:
                result.add(k)
        for e in other.table:
            for k in e:
                result.add(k)
        return result

    def __and__(self, other):
        result = Set()
        for e in other.table:
            for k in e:
                if self.search(k) is not None:
                    result.add(k)
        return result

    def __sub__(self, other):
        result = Set()
        for e in self.table:
            for k in e:
                if other.search(k) is None:
                    result.add(k)
        return result

    def __len__(self):
        return self.n

    def __iter__(self):
        for bucket in self.table:
            if bucket is not None:
                for key in bucket:
                    yield key
