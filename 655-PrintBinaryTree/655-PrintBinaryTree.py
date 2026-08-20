# Last updated: 8/20/2026, 2:10:08 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def height(root):
            if not root:
                return 0
            
            return 1 + max(height(root.left), height(root.right))

        def fill(matrix, node, r, c, height):

            if not node:
                return

            matrix[r][c] = str(node.val)
            d = 2 ** (height - r - 1)
            fill(matrix, node.left, r+1, c - d, height)
            fill(matrix, node.right, r+1, c + d, height)

        m = height(root)
        n = 2 ** m - 1
        matrix = [["" for _ in range(n)] for _ in range(m)]
        
        fill(matrix, root, 0, (n - 1) // 2, m-1)
        return matrix
        