# Last updated: 8/20/2026, 2:10:20 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            size = len(queue)
            temp = 0
            for i in range(size):
                node = queue.popleft()
                temp += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            result.append(temp / size)
            
        return result
        
        