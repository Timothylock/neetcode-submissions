# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.topDiameter(root)) - 1
        
    def topDiameter(self, root):
        # Our own max diameter, our longest length
        if root == None:
            return 0, 0

        lm, ld = self.topDiameter(root.left)
        rm, rd = self.topDiameter(root.right)

        return max(lm, rm, (ld + rd) + 1), max(ld, rd) + 1
        
        