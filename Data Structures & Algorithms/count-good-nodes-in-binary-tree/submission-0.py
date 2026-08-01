# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, path_max):
            if not node: return 0
            good = 1 if node.val >= path_max else 0
            m = max(path_max, node.val)
            return good + dfs(node.left, m) + dfs(node.right, m)
        return dfs(root,root.val)