# Last updated: 8/20/2026, 2:06:19 AM
class TrieNode:
    
    def __init__(self, name):
        self.hm = defaultdict(TrieNode)
        self.name = name
        self.value = -1
        

class FileSystem:

    def __init__(self):
        self.root = TrieNode("")
        

    def createPath(self, path: str, value: int) -> bool:
        components = path.split("/")
        
        curr = self.root
        
        for i in range(1, len(components)):
            name = components[i]
            
            if name not in curr.hm:
                if i == len(components) - 1:
                    curr.hm[name] = TrieNode(name)
                else: return False
                
            curr = curr.hm[name]
            
        if curr.value != -1:
            return False
        
        curr.value = value
        return True

    def get(self, path: str) -> int:
        
        curr = self.root
        components = path.split("/")
        
        for i in range(1, len(components)):
            name = components[i]
            if name not in curr.hm:
                return -1
            
            curr = curr.hm[name]
        return curr.value
        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)