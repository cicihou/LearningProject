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
    HashMap <Integer, ListNode> cache = new HashMap<>();
    Random rand = new Random();
    int i = 0;

    public Solution(ListNode head) {
        while (head != null) {
            cache.put(i, head);
            head = head.next;
            i++;
        }
    }

    public int getRandom() {
        return this.cache.get(rand.nextInt(i)).val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
