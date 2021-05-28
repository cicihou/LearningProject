class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        '''
        method 1
        I write this answer(method 1) intuitively
        the leetcode accpet this answer while I find it should not
        I've submitted the issue for adding the testcase
        https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/3657

        if set(a) != set(b): return -1 will help it become faster
        actually if a = "dbeg", b = "egb", it will return wrong (testcases missing)

        这个方法是错的，帮 leetcode 提了一个 testcase
        '''
        # if b in a:
        #     return 1
        #
        # # this line could help it run more fast, but actually it should not work
        # # need a testcase like a = "dbeg", b = "egb"
        # if set(a) != set(b):
        #     return -1
        # tmp = a
        # count = 1
        # for i in range(len(a) + len(b)):
        #     if b in a:
        #         return count
        #     a += tmp
        #     count += 1
        #
        # return -1


        '''
        method 2
        optimize method 1
            2.1 correct set() statement error
            2.2 reduce the iteration times
        '''
        if b in a:
            return 1
        if not set(b).issubset(set(a)):
            return -1
        tmp = a
        count = 1

        # 这一行遍历使速度快了十倍以上，只需要很少的遍历
        for i in range(1, len(b) // len(a) + 3):
            if b in a:
                return count
            a += tmp
            count += 1

        return -1


        '''
        method 3
        https://leetcode.com/problems/repeated-string-match/discuss/330741/Simple-Python3-Solution-(beats-~100)-(my-first-post-on-LeetCode-!!!)
        '''
        # TODO


s = Solution()

testcases = {
    3: [
        ["abcd", "cdabcdab"]
    ],
    2: [
        ["a", "aa"],
        ["aaaaaaaaaaaaaaaaaaaaaab", "ba"],
        ["dbeg", "gd"]
    ],
    1: [
        ["a", "a"]
    ],
    -1: [
        ["abc", "wxyz"],
        ["abcabcabcabc", "abac"],
        ["abcabcabcabc", "abac"],
        ['a' * 9998, 'a' * 9998 + 'ba'],
    ],
    4: [
        ["abc", "cabcabca"]
    ],

}


for k, v in testcases.items():
    for i in range(len(v)):
        a, b = v[i]
        res = s.repeatedStringMatch(a, b)
        if res != k:
            print(k, i)
