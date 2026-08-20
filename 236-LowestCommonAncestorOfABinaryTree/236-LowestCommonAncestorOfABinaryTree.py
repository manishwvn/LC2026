# Last updated: 8/20/2026, 2:15:08 AM
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                return node

            if left and right:
                return node

            return left or right

        return dfs(root)