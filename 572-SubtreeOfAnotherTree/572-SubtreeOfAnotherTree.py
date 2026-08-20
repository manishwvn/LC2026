# Last updated: 8/20/2026, 2:11:20 AM
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtree_hashes = set()

        def serializeNode(node):
            if not node:
                return "N"
            else:
                return f"({node.val},{serializeNode(node.left)},{serializeNode(node.right)})"
        return serializeNode(subRoot) in serializeNode(root)