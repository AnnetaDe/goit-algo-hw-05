class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def print_it(self):
        for index, value in enumerate(self.table):
            print(index, value)

    def delete(self, key):
        key_hash = self.hash_function(key)
        for index, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                self.table[key_hash].pop(index)
                return True
        return False


H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.hash_function("pineapple")


print(H.get("apple"))
print(H.get("orange"))
print(H.get("banana"))
H.print_it()
H.delete("banana")
H.print_it()
