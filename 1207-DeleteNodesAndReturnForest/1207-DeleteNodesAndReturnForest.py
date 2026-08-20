# Last updated: 8/20/2026, 2:05:27 AM
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        delete_set = set(to_delete)
        forest = []
        stack = [(root, None, False)]  # (node, parent, visited)

        while stack:
            node, parent, visited = stack.pop()

            if not node:
                continue

            if visited:
                # Post-order: children already processed
                if node.val in delete_set:
                    # Cut connection from parent
                    if parent:
                        if parent.left == node:
                            parent.left = None
                        elif parent.right == node:
                            parent.right = None

                    # Add non-null children to forest
                    if node.left:
                        forest.append(node.left)
                    if node.right:
                        forest.append(node.right)
                else:
                    # Not deleted — do nothing (kept in place)
                    pass
            else:
                # Push node back to stack for post-processing
                stack.append((node, parent, True))
                # Push right and left children for traversal
                stack.append((node.right, node, False))
                stack.append((node.left, node, False))

        if root.val not in delete_set:
            forest.append(root)

        return forest