class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int direc = 0;
        int left = 0;
        int right = matrix[0].length - 1;
        int top = 0;
        int down = matrix.length - 1;
        ArrayList<Integer> res = new ArrayList<>();

        while (left <= right && top <= down) {
            if (direc == 0){
                for (int i=left; i<right+1; i++) {
                    res.add(matrix[top][i]);
                }
                top++;
            } else if (direc == 1){
                for (int i=top; i<down+1; i++) {
                    res.add(matrix[i][right]);
                }
                right--;
            } else if (direc == 2){
                for (int i=right; i>left-1; i--){
                    res.add(matrix[down][i]);
                }
                down--;
            } else if (direc == 3){
                for (int i=down; i>top-1; i--){
                    res.add(matrix[i][left]);
                }
                left++;
            }
            direc = (direc + 1) % 4;
        }
        return res;
    }
}
