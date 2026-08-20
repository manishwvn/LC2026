# Last updated: 8/20/2026, 2:00:58 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            nonlocal p_flag, q_flag
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                if node == p:
                    p_flag = True
                else:
                    q_flag = True

                return node

            if left and right:
                return node
            else:
                return left or right

        
        p_flag, q_flag = False, False
        ans = dfs(root)

        return ans if p_flag and q_flag else None
        