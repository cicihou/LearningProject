/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */


class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<>();
        dfs(res, root);
        return res;
    }

    public void dfs(ArrayList res, TreeNode root) {
    // 当返回标明了是 void，就不需要显式的 return null
        if (root != null) {
            dfs(res, root.left);
            res.add(root.val);
            dfs(res, root.right);
        }
    }
}
