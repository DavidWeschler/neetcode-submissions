# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftDepth = checkBalance(root.left)
            if leftDepth == -1:
                return -1
            
            rightDepth = checkBalance(root.right)
            if rightDepth == -1:
                return -1
            
            if abs(leftDepth - rightDepth) > 1:
                return -1
            
            return 1 + max(leftDepth, rightDepth)
        return checkBalance(root) != -1