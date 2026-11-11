# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if root is None:
            return []

        res = []
        queue = [root]
        while queue:
            levelSize = len(queue)
            cur = []

            for i in range(levelSize):
                node = queue.pop(0)
                cur.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            res.append(cur)
        
        return res

        