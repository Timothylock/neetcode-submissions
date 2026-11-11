# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.rIsValidBST(root, -1 * math.inf, math.inf)
    
    def rIsValidBST(self, root, biggerThan, smallerThan):
        if root is None:
            return True

        if root.val <= biggerThan or root.val >= smallerThan:
            return False

        res = True
        res = res and self.rIsValidBST(root.left, biggerThan, root.val)
        res = res and self.rIsValidBST(root.right, root.val, smallerThan)
        return res