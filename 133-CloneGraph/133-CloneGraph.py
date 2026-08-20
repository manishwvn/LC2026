# Last updated: 8/20/2026, 2:17:18 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(node):
            newNode = Node(node.val)
            hm[node] = newNode
            
            for n in node.neighbors:
                if n not in hm:
                    dfs(n)
                    
                hm[node].neighbors.append(hm[n])
        
        
        if not node: return None
        
        hm = {}
        dfs(node)
        return hm[node]
        
    
        