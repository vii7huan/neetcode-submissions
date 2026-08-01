# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True              # empty subRoot is always a subtree
        if not root:
            return False             # ran out of tree, no match found

        if self.isSameTree(root, subRoot):
            return True              # found a match rooted here

        # otherwise, keep searching in the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True              # both empty → identical
        if not p or not q or p.val != q.val:
            return False             # one empty, or values differ → not identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)