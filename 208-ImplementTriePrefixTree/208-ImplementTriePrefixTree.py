# Last updated: 8/20/2026, 2:15:49 AM
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        
        curr = self.trie
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
            
        curr.isEnd = True
    
    def search(self, word: str) -> bool:
        curr = self.trie
        
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)