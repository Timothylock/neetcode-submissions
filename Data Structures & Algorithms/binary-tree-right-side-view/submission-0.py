# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS, last item
        if root is None:
            return []

        res = []
        queue = [root]

        while queue:
            curLen = len(queue)

            for i in range(curLen):
                node = queue[i]
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            res.append(queue[curLen - 1].val)
            queue = queue[curLen:]

        return res