class Solution {
    public int romanToInt(String s) {
        // java 中 initial hashmap 的写法
        HashMap <Character, Integer> cache = new HashMap<>() {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};

        int res = 0;
        for (int i=0; i < s.length() - 1; i++) {
            Integer j = cache.get(s.charAt(i));
            if (j < cache.get(s.charAt(i+1))) {
                res = res - j;
            } else {
                res = res + j;
            }
        }
        return res + cache.get(s.charAt(s.length() - 1));
    }
}
