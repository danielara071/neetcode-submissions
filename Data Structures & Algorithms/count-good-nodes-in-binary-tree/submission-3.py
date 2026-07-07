# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxi):
            if not node:
                return
            if node.val >= maxi:
                self.count += 1
            maxi = max(node.val, maxi)
            left = dfs(node.left, maxi)
            right = dfs(node.right, maxi)
        maxi = float("-inf")
        dfs(root, maxi)
        return self.count
            