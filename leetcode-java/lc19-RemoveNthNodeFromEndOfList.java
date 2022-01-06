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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        ListNode slow = dummy;
        ListNode fast = dummy;

        while (n>0) {
            fast = fast.next;
            n--;
        }
        while (fast != null && fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }

        if (slow.next == null){
            slow.next = null;
        } else {
            slow.next = slow.next.next;
        }
        return dummy.next;
    }
}
