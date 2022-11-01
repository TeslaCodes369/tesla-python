class HashTable:
    def __init__(self) -> None:
        self.capacity = 100
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hashFunction(self, key):
        sum = 0
        for ch in key:
            sum += ord(ch)

        return sum % self.capacity

    def insert(self, key, val):
        index = self.hashFunction(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = val
                return

            index = (index + 1) % self.capacity

        self.keys[index] = key
        self.values[index] = val

    def get(self, key):
        index = self.hashFunction(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        return None


if __name__ == '__main__':
    table = HashTable()
    table.insert('anil', 100)
    table.insert('asdf', 500)
    table.insert('asdf', 800)

    print(table.get('anil'))
    print(table.get('anil1'))
    print(table.get('anil2'))
    print(table.get('asdf'))
