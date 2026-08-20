# Last updated: 8/20/2026, 2:18:10 AM
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1, stack2 = [p], [q]

        while stack1 and stack2:
            node1, node2 = stack1.pop(), stack2.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            # Push in the same order
            stack1.append(node1.right)
            stack2.append(node2.right)
            stack1.append(node1.left)            
            stack2.append(node2.left)

        return not stack1 and not stack2  # check if both stacks are empty