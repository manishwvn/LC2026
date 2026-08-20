# Last updated: 8/20/2026, 2:17:46 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def preorder(node):
            if not node:
                return None
            
            if not node.left and not node.right:
                return node
            
            left_end = preorder(node.left)
            right_end = preorder(node.right)
            
            if left_end:
                left_end.right = node.right
                node.right = node.left
                node.left = None
                
            return right_end if right_end else left_end
            
        if not root: return None
        preorder(root)
        