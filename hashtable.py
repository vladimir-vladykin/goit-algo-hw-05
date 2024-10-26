
def main():
    table = HashTable(5)
    print(f"Initial state of hashtable:\n{table.table}")
    print("\n")
    
    table.insert("apple", 10)
    table.insert("orange", 20)
    table.insert("banana", 30)
    table.insert("apple", 50)

    print(f"State of hashtable after all inserts:\n{table.table}")
    print("\n")

    print(f"Apple value is {table.get('apple')}") 
    print(f"Orange value is {table.get('orange')}") 
    print(f"Banana value is {table.get('banana')}") 
    print("\n")

    # remove element, and check is it still in hastable
    table.delete("apple")
    print(f"Apple value after delete from hastable is {table.get('apple')}")  # None is expected here
    print(f"Final state of hashtable after delete Apple:\n{table.table}")


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
    

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    # remove this element
                    self.table[key_hash].pop(i)
                    return True
        return False
    

if __name__ == '__main__':
    main()