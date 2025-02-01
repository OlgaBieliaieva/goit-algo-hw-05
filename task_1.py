class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if not self.table[key_hash]: 
            self.table[key_hash].append(key_value)
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:  
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)  
    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for index, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][index]
                    return True
        return False

# Тестування хеш-таблиці
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("Before deletion:")
print("apple:", H.get("apple"))  # Виведе: 10
print("orange:", H.get("orange"))  # Виведе: 20
print("banana:", H.get("banana"))  # Виведе: 30

# Видалення ключів
H.delete("orange")
H.delete("apple")

print("\nAfter deletion:")
print("apple:", H.get("apple"))  # Виведе: None
print("orange:", H.get("orange"))  # Виведе: None
print("banana:", H.get("banana"))  # Виведе: 30