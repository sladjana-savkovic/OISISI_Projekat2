
class Set(object):

    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict[key]=value

    def ret_key(self):
        return self.dict.keys()

    def ret_val(self, key):
        if self.dict.get(key) is not None:
            return self.dict[key]
        return None

    def inc_value(self, key):
        self.dict[key] += 1

    def __len__(self):
        return len(self.dict)

    def __iter__(self):
        return iter(self.dict.copy())

    def __contains__(self, e):
        if self.dict.get(e) is not None:
            return True

        else:
            return False
    def remove(self,e):
        del self.dict[e]

    def __or__(self, other):
        result = Set()
        for e in self.ret_key():
            result.add(e,e)
        for e in other.ret_key():
            result.add(e,e)
        return result

    def __and__(self, other):
        result = Set()
        for e in other.ret_key():
            if e in self.ret_key():
                result.add(e,e)
        return result

    def __sub__(self, other):
        result = Set()
        for e in self.ret_key():
            if e not in other.ret_key():
                result.add(e,e)
        return result

    def __str__(self):
        a=""
        for e in self.dict:
            a += str(e)+ " " + str(self.dict[e]) + "\n"
        return a