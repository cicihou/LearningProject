class Solution {
    public boolean isValid(String s) {
        Stack <Character> stack = new Stack<Character>();
        HashMap <Character, Character> cache = new HashMap<>();
        // 这里除了一个个添加，也可以初始化定义，注意 java 里面单个字符的类型是 character，并且要用单引号
        cache.put(')', '(');
        cache.put('}', '{');
        cache.put(']', '[');
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (!stack.isEmpty() && cache.containsKey(c) && cache.get(c) == stack.peek()) {
                stack.pop();
            } else {
                stack.add(c);
            }
        }
        return stack.isEmpty();
    }
}
