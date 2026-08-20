# Last updated: 8/20/2026, 2:12:13 AM
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        prev = None
        curr_count = 0
        max_count = 0
        modes = []

        def handle_node(val):
            nonlocal prev, curr_count, max_count, modes
            if val == prev:
                curr_count += 1
            else:
                curr_count = 1
                prev = val

            if curr_count > max_count:
                max_count = curr_count
                modes = [val]
            elif curr_count == max_count:
                modes.append(val)

        while curr:
            if not curr.left:
                handle_node(curr.val)
                curr = curr.right
            else:
                # Find the predecessor of curr
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                # Make curr the right child of its predecessor
                if not predecessor.right:
                    predecessor.right = curr
                    curr = curr.left
                # Restore the original tree structure
                else:
                    predecessor.right = None
                    handle_node(curr.val)
                    curr = curr.right

        return modes