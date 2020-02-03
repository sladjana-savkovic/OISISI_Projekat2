
class Set(object):
    def __init__(self):
        self.lista = []

    def add(self, e):
        if not e in self.lista:
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
        if e in self.lista:
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
            if e in self.lista:
                result.add(e)
        return result

    def __sub__(self, other):
        result = Set()
        for e in self:
            if e not in other:
                result.add(e)
        return result

    def __str__(self):
        a=""
        for e in self.lista:
            a += str(e) + "\n"
        return a