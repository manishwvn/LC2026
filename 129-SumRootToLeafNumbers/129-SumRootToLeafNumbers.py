# Last updated: 8/20/2026, 2:17:23 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current):
            nonlocal result
            if not node:
                return

            current = current * 10 + node.val

            if not node.left and not node.right:
                result += current
                return 

            left = dfs(node.left, current)
            right = dfs(node.right, current)
            

        result = 0
        dfs(root, 0)
        return result