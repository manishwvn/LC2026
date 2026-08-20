# Last updated: 8/20/2026, 2:08:40 AM
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash_map = [[] for _ in range(self.size)]
    
    def hash(self, key):
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        i = 0

        while i < len(self.hash_map[index]):
            k, v = self.hash_map[index][i]
            if k == key:
                self.hash_map[index][i] = (key, value)
                return
            i += 1
        self.hash_map[index].append((key, value))
    
    def get(self, key: int) -> int:
        index = self.hash(key)

        for k, v in self.hash_map[index]:
            if k == key:
                return v
        
        return -1
        
    def remove(self, key: int) -> None:
        index = self.hash(key)
        i = 0

        while i < len(self.hash_map[index]):
            k, v = self.hash_map[index][i]
            
            if k == key:
                del self.hash_map[index][i]
                return
            else:
                i += 1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)