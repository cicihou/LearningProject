class Solution {
    List<String> res = new ArrayList<>();
    int n;
    public List<String> generateParenthesis(int n) {
        StringBuilder path = new StringBuilder();
        this.n = n;
        backtrack(path, 0, 0);
        return res;
    }

    public void backtrack(StringBuilder path, int left, int right) {
        if (path.length() == 2 * n) {
            res.add(path.toString());
        } else {
            if (left < n) {
                path.append('(');
                backtrack(path, left+1, right);
                path.deleteCharAt(path.length() - 1);
            }
            if (right < left) {
                path.append(')');
                backtrack(path, left, right+1);
                path.deleteCharAt(path.length() - 1);
            }
        }
    }
}
