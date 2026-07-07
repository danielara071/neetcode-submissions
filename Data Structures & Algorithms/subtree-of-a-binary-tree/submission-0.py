# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root and subRoot:
                return False
            elif root and not subRoot:
                return False
            elif root.val != subRoot.val:
                return False
            left = dfs(root.left, subRoot.left)
            right = dfs(root.right, subRoot.right)
            return left and right
        if not subRoot:
            return True
        if not root:
            return False

        if dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

