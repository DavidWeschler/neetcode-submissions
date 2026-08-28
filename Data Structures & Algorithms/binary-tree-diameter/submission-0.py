# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftMax = maxDepth(root.left)
            rightMax = maxDepth(root.right)
            
            self.diameter = max(self.diameter, leftMax + rightMax)
            
            return 1 + max(leftMax, rightMax) 
        
        maxDepth(root)
        return self.diameter