# Last updated: 8/20/2026, 2:06:51 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        queue = deque()
        queue.append(root)
    
        while queue:
            size = len(queue)
            x_found = False
            y_found = False

            for i in range(size):
                node = queue.popleft()

                if node.val == x:
                    x_found = True
                if node.val == y:
                    y_found = True

                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if x_found and y_found:
                return True

        return False
