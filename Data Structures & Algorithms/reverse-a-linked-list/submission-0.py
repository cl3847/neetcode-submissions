# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node, acc):
            if not node:
                return acc
            else:
                return rev(node.next, ListNode(node.val, acc))

        return rev(head, None)
        