# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pF, qF, lca = self.rLowestCommonAncestor(root, p, q)
        return lca
        

    # returns pFound, qFound, LCA
    def rLowestCommonAncestor(self, root, p, q): 
        if root is None:
            return False, False, None

        pF = root == p
        qF = root == q
        
        pFl, qFl, lca = self.rLowestCommonAncestor(root.left, p, q)
        if lca is not None:
            return True, True, lca

        pFr, qFr, lca = self.rLowestCommonAncestor(root.right, p, q)
        if lca is not None:
            return True, True, lca
        
        pFound = pF or pFl or pFr
        qFound = qF or qFl or qFr
        if pFound and qFound:
            return True, True, root
        
        return pFound, qFound, None