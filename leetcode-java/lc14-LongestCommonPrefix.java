class Solution {
    public String longestCommonPrefix(String[] strs) {
        // string 的 length() 是方法，array 的 length 是属性
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].length() == i || strs[j].charAt(i) != c) {
                    return strs[j].substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
