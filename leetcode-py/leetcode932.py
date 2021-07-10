'''
由数字的奇偶特性，可知：奇数 + 偶数 = 奇数 。

因此如果要使得：**对于每个  i < j，都不存在  k 满足  i < k < j  使得  A[k] * 2 = A[i] + A[j] ** 成立，
                我们可以令 A[i] 和 A[j] 一个为奇数，另一个为偶数即可。

另外还有两个非常重要的性质，也是本题的突破口。那就是：

性质 1： 如果数组 A 是 漂亮数组，那么将 A 中的每一个数 x 进行 kx + b 的映射，其仍然为漂亮数组。
        其中 k 为不等于 0 的整数， b 为整数。
性质 2：如果数组 A 和 B 分别是不同奇偶性的漂亮数组，那么将 A 和 B 拼接起来仍为漂亮数组。

举个例子。我们要求长度为 N 的漂亮数组。那么一定是有 N / 2 个偶数 和 N - N / 2 个奇数。

这里的除法为整除。

假设长度为 N / 2 和 N - N/2 的漂亮数组被计算出来了。
那么我们只需要对长度为 N/2 的漂亮数组通过性质 1 变换成全部为偶数的漂亮数组，并将长度为 N - N/2 的漂亮数组也通过性质 1 变换成全部为奇数的漂亮数组。
接下来利用性质 2 将其进行拼接即可得到一个漂亮数组。

刚才我们假设长度为 N / 2 和 N - N/2 的漂亮数组被计算出来了，实际上我们并没有计算出来，那么其实可以用同样的方法来计算。
其实就是分治，将问题规模缩小了，问题本质不变。递归的终点自然是 N == 1，此时可直接返回 [1]。


代码：https://leetcode-solution.cn/solutionDetail?type=3&id=62&max_id=2

本题不太理解
'''


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        '''
        time: O(nlogn)
        space: O(n+logn)
        :param n:
        :return:
        '''
        memo = {1: [1]}
        def f(n):
            if n not in memo:
                odds = f((n+1)//2)
                evens = f(n//2)
                memo[n] = [2*x - 1 for x in odds] + [2*x for x in evens]
            return memo[n]
        return f(n)
