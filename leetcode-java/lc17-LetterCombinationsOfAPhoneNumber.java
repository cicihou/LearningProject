class Solution {
    // 在 jdk 9 之后可以用 Map.of 来直接创造 immutable variable，简化写法
    HashMap <Character, String> cache = new HashMap<>() {{
        put('2', "abc");
        put('3', "def");
        put('4', "ghi");
        put('5', "jkl");
        put('6', "mno");
        put('7', "pqrs");
        put('8', "tuv");
        put('9', "wxyz");
    }};

    // List contains ArrayList and LinkedList, java 类型中超集覆盖了子集可定义，反之不行
    List <String> res = new ArrayList<>();
    String digits;

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return res;
        }

        StringBuilder path = new StringBuilder();

        // 局部变量覆盖到全局的方法
        this.digits = digits;

        backtrack(0, path);
        return res;
    }

    public void backtrack(int index, StringBuilder path) {
        if (index == digits.length()) {
            res.add(path.toString());
        } else {
            // 注意 StringBuilder 的一些方法
            String options = cache.get(digits.charAt(index));
            for (char option: options.toCharArray()) {
                path.append(option);
                backtrack(index+1, path);
                path.deleteCharAt(path.length() - 1);
            }
        }
    }
}
