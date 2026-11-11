# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt, final = self.dfs(root, k, 0)
        return final
        
    # count, finalValue
    def dfs(self, root: Optional[TreeNode], k: int, cnt: int):
        if root is None:
            return cnt, -1

        cnt, final = self.dfs(root.left, k, cnt)
        if final != -1:
            return -1, final
        if cnt >= k:
            print("ERROR: cnt > k without final getting returned")

        # Count ourselves as one, but only after left
        cnt += 1
        if cnt == k:
            return -1, root.val
        
        cnt, final = self.dfs(root.right, k, cnt)
        return cnt, final
        