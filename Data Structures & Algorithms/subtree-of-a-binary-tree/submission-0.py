class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sR = self.generateSerialization(root)
        sRR = self.generateSerialization(subRoot)
        return sRR in sR

    def generateSerialization(self, root) -> str:
        if root is None:
            return ",#"

        return "," + str(root.val) + self.generateSerialization(root.left) + self.generateSerialization(root.right)