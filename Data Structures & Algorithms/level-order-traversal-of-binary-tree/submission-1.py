# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            q = collections.deque()
            q.append(root)
            order = []
            while q:
                level = []
                qlen = len(q)
                for i in range(qlen):
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                if level:
                    order.append(level)
                
            return order
        
        return bfs(root)
