# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def h(root):
            if not root:
                return True
            left,right = h(root.left), h(root.right)
            if left == -1:
                return -1
            if right == -1 or abs(left - right) > 1:
                return -1
            return 1+ max(left,right)
        return h(root)!= -1