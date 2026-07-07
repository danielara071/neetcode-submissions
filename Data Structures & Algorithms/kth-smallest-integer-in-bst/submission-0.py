# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.kth = None
        self.cnt = 1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kay = k
        def dfs(root):
            if root.left:
                left = dfs(root.left)
            if not root:
                return
            if self.cnt == kay:
                self.kth = root.val
            self.cnt += 1
            #something
            if root.right:
                right = dfs(root.right)
        dfs(root)
        return self.kth


