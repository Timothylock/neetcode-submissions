# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N"

        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataArr = data.split(",")
        _, res = self.dfs(dataArr, 0)
        return res
        
    def dfs(self, data, i): 
        # returns i in data and treenode
        if data[i] == "N":
            return i + 1, None

        tn = TreeNode(data[i])
        i, tnl = self.dfs(data, i + 1)
        i, tnr = self.dfs(data, i)
        tn.left = tnl
        tn.right = tnr

        return i, tn

