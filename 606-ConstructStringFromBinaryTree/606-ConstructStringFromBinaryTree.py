# Last updated: 8/20/2026, 2:10:51 AM

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(curNode):
            if not curNode:
                return ''

            subString = str(curNode.val)
            #If curNode has no children
            if not curNode.left and not curNode.right:
                return subString

            subString += '(' + solve(curNode.left) + ')'
            if curNode.right:
                subString += '(' + solve(curNode.right) + ')'

            return subString

        return solve(root)