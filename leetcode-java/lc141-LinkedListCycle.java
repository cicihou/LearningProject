/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashMap <ListNode, Integer>cache = new HashMap<>();
        while (head != null) {
            if (cache.get(head) != null) {
                return true;
            } else {
                cache.put(head, 0);
                head = head.next;
            }
        }
        return false;

    }
}
