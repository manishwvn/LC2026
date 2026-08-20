# Last updated: 8/20/2026, 2:17:54 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            nonlocal balanced
            if not root:
                return 0
            
            l_h = height(root.left)
            r_h = height(root.right)

            if abs(l_h - r_h) > 1:
                balanced = False
                return 0
            
            return 1 + max(l_h, r_h)

        balanced = True
        height(root)
        return balanced