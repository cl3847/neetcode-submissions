# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def stringify(n):
            if not n:
                return "n"
            else:
                return f"{n.val}{stringify(n.left)}{stringify(n.right)}"
        
        return stringify(p) == stringify(q)