# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.goodNodesR(root, root.val)

    def goodNodesR(self, root, maxSoFar):
        if root is None:
            return 0

        cur = 0
        if root.val >= maxSoFar:
            cur += 1
            maxSoFar = root.val

        cur += self.goodNodesR(root.left, maxSoFar)
        cur += self.goodNodesR(root.right, maxSoFar)

        return cur
        