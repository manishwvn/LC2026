# Last updated: 8/20/2026, 2:17:49 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, path_sum, targetSum):
            if not root:
                return False
            
            if not root.left and not root.right:
                if path_sum == targetSum:
                    return True
                
            left_val = right_val = False
            if root.left:
                left_val = dfs(root.left, path_sum + root.left.val, targetSum)
            
            if root.right:
                right_val = dfs(root.right, path_sum + root.right.val, targetSum)
            
            return left_val or right_val
        
        if not root:
            return False
        
        return dfs(root, root.val, targetSum)
        