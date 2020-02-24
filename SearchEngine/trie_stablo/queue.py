#Pomocna klasa koja se koristi za obilazak stabla po sirini

class QueueError(Exception):
    pass

class Queue(object):
    #Klasa modeluje red na osnovu liste.
    def __init__(self, capacity=10):
        self._size = 0
        self._first = 0
        self._capacity = capacity
        self._data = [None]*self._capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise QueueError('Red je prazan.')
        return self._data[self._first]

    def dequeue(self):
        if self.is_empty():
            raise QueueError('Red je prazan.')

        element = self._data[self._first]

        self._data[self._first] = None

        self._first = (self._first+1) % self._capacity
        self._size -= 1

        if 0 < self._size < self._capacity//4:
            self._resize(self._capacity//2)

        return element

    def enqueue(self, e):
        if self._size == self._capacity:
            self._resize(2*self._capacity)

        index = (self._first+self._size) % self._capacity
        self._data[index] = e
        self._size += 1

    def _resize(self, capacity):
        current_data = self._data
        current_first = self._first

        self._data = [None]*capacity

        for k in range(self._size):
            self._data[k] = current_data[current_first]
            current_first = (current_first+1) % len(current_data)

        self._first = 0
        self._capacity = capacity