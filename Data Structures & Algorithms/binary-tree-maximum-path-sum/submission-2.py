# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, res = self.dfs(root)
        return res
        

    def dfs(self, root):
        if root is None:
            return 0, -float('inf')
        
        # Return max down one path, and the max total from that node
        leftSP, leftMax = self.dfs(root.left)
        rightSP, rightMax = self.dfs(root.right)

        leftSP = max(leftSP, 0)
        rightSP = max(rightSP, 0)

        maxSP = max(leftSP, rightSP) + root.val
        maxTotal = max(leftMax, rightMax, leftSP + root.val + rightSP)

        return maxSP, maxTotal
