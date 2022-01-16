class Solution {
    int res = 0;
    int n;
    HashSet<Integer> columns = new HashSet<Integer>();
    HashSet<Integer> upward_diagonal = new HashSet<Integer>();
    HashSet<Integer> downward_diagonal = new HashSet<Integer>();

    public int totalNQueens(int n) {
        this.n = n;

        backtrack(0);
        return res;
    }

    public void backtrack(int row) {
        if (row == n) {
            res ++;
        } else {
            for (int col = 0; col < n; col++) {
                if (!columns.contains(col) && !upward_diagonal.contains(col+row) && !downward_diagonal.contains(col-row)){
                    columns.add(col);
                    upward_diagonal.add(col+row);
                    downward_diagonal.add(col-row);
                    backtrack(row+1);
                    columns.remove(col);
                    upward_diagonal.remove(col+row);
                    downward_diagonal.remove(col-row);
                }
            }
        }
    }
}
