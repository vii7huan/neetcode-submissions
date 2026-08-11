"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        clones = {}
        def dfs(n):
            if n in clones:
                return clones[n]
            copy = Node(n.val)
            clones[n] = copy
            copy.neighbors = [dfs(nb) for nb in n.neighbors]
            return copy
        return dfs(node)