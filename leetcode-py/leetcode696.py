'''
视频：https://www.youtube.com/watch?v=MGPHPadxhtQ
一个非常好的讲解，4:00 处有图，一看就懂

计算个数是不去重的，也就是说 10101 有四个 substrings

"10" "01" "10" "01"

因此我们只要用两个指针，指针维护的一个是全0/1 的区间起点，另一个维护的是全 0/1 的区间终点
并计算在这两个指针构成的区间中 0 和 1 的个数
min(count0, count1)

如何确定这两个指针的指向

'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1
        res += min(prev, curr)  # 最后一个sliding window 没有被统计就退出的循环
        return res
