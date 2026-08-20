# Last updated: 8/20/2026, 2:01:54 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        sum_ = 0
        
        for node in tree:
            sum_ += node.val
            
            for child in node.children:
                sum_ -= child.val
        
        for node in tree:
            if sum_ == node.val:
                return node
        