from data import Data


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key, rehash_flag: bool = False):
        if rehash_flag:
            return key % (self.size * 2)
        else:
            return key % self.size

    def add(self, data: Data):
        if self.get_value(data.key) is None:
            index = self.hash_function(data.key)

            self.table[index] = data
        else:
            self.rehash()
            self.add(data)

    def remove(self, data: Data):
        index = self.hash_function(data.key)

        self.table[index] = None

    def get_value(self, key):
        index = self.hash_function(key)

        return self.table[index]

    def rehash(self):
        buffer_table = HashTable(self.size*2)

        for i in range(len(self.table)):
            if self.table[i]:
                index = self.hash_function(self.table[i].key, True)
                buffer_table.table[index] = self.table[i]

        self.table = buffer_table.table
        self.size = buffer_table.size

    def print_table(self):
        for i in range(len(self.table)):
            if self.table[i] is None:
                print(f"{i}: {self.table[i]}")
            else:
                print(f"{i}: ", end='')
                self.table[i].print_data()
        print()
