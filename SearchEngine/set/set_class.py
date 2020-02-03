
class Set(object):
    def __init__(self):
        self.lista = []

    def add(self, e):
        if not self.lista.__contains__(e):
            self.lista.append(e)

    def __contains__(self, e):
        if e in self.lista:
            return True
        else:
            return False

    def __len__(self):
        return len(self.lista)

    def __iter__(self):
        for e in self.lista:
            yield e

    def remove(self,e):
        if self.lista.__contains__(e):
            self.lista.remove(e)
        else:
            raise KeyError("Element ne postoji u skupu!")

    def __or__(self, other):
        result = Set()
        for e in self:
            result.add(e)
        for e in other:
            result.add(e)
        return result

    def __and__(self, other):
        result = Set()
        for e in other:
            if self.lista.__contains__(e):
                result.add(e)
        return result

    def minus(self, other):
        result = Set()
        for e in self:
            if e not in other:
                result.add(e)
        return result