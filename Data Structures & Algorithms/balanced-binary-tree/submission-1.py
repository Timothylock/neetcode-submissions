# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.isBalancedT(root)
        return balanced

    def isBalancedT(self, root):
        if root is None:
            return True, 0

        leftBalanced, leftHeight = self.isBalancedT(root.left)
        rightBalanced, rightHeight = self.isBalancedT(root.right)

        maxHeight = max(leftHeight, rightHeight) + 1

        if not leftBalanced or not rightBalanced:
            return False, maxHeight

        if abs(leftHeight - rightHeight) > 1:
            return False, maxHeight

        return True, maxHeight
