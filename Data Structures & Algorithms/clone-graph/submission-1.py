"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        def dfs(start):
            stack = deque()
            visited = set()
            dic = {}
            dic[start] = Node(start.val)
            stack.append(start)
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for nei in node.neighbors:
                        if nei not in dic:
                            dic[nei] = Node(nei.val)
                            stack.append(nei)
                        dic[node].neighbors.append(dic[nei])
            return dic[start]
        
        return dfs(node)        
            