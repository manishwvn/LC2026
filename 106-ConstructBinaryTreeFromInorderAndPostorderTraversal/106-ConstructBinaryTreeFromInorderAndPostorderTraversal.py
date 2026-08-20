# Last updated: 8/20/2026, 2:17:58 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        hm = {}
    
        for i, val in enumerate(inorder):
            hm[val] = i
    
        def helper(inorder, postorder, inStart, inEnd, postStart, postEnd):

                if inStart > inEnd or postStart > postEnd:
                    return None

                rootVal = postorder[postEnd]
                root = TreeNode(rootVal)
                index = hm[rootVal]


                root.left = helper(inorder, postorder, inStart, index-1, postStart, postStart + index - inStart - 1)
                root.right = helper(inorder, postorder, index+1, inEnd, postStart + index - inStart, postEnd-1)

                return root



        return helper(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
        