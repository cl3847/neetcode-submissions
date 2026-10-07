/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode helper(ListNode head, ListNode acc) {
        if (head == null) {
            return null;
        } else if (head.next == null) {
            head.next = acc;
            return head;
        } else {
            ListNode next = head.next;
            head.next = acc;
            return helper(next, head);
        }
    }

    public ListNode reverseList(ListNode head) {
        return helper(head, null);
    }
}
