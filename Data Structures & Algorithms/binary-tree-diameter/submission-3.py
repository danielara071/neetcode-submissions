# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxi = float("-inf")

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxi = max(self.maxi, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.maxi
        