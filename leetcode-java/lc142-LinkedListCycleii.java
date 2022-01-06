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
    public ListNode detectCycle(ListNode head) {
        HashMap <ListNode, Integer>cache = new HashMap<>();
        while (head != null) {
            if (cache.get(head) != null){
                return head;
            } else {
                cache.put(head, 0);
                head = head.next;
            }
        }
        return null;
    }
}
