# Creating Hashtable as a nested list.

class Hash:
    def __init__(self, size) -> None:
        self.size = size
        self.HashTable = [[] for _ in range(size)]

    # Hashing Function to return
    # key for every value.
    def Hashing(self, keyvalue):
        return keyvalue % self.size

    # Insert Function to add
    # values to the hash table
    def insert(self, keyvalue, value):

        hash_key = self.Hashing(keyvalue)
        self.HashTable[hash_key].append(value)

    # Function to display hashtable
    def display_hash(self):

        for i in range(self.size):
            print(i, end=" ")

            for j in self.HashTable[i]:
                print("-->", end=" ")
                print(j, end=" ")

            print()
