# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inv(n):
            if n:
                l = inv(n.right)
                r = inv(n.left)
                return TreeNode(n.val, l, r)

        return inv(root)