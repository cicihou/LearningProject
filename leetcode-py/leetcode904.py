from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ''' 这题题目上弯弯绕绕，其实就是
        给一个数组， 让你选定一个子数组， 这个子数组最多只有两种数字，这个选定的子数组长度最大可以是多少
        '''
        def atMostK(k, nums):
            '''
            i 和 j 实质上都是记录坐标:
            j 记录的是自增的数组顺序坐标
            i 记录的是最先进入滑动窗口的果树

            j - i + 1 反应的是当前的连续的子数组的最大值

            设 win 为一个只包含两种果树的滑动窗口 sliding window
            1. 如果 nums[j] 在 win 的对应的值为 0 ，则当前的滑动窗口不含有这种果树，将篮子 k 的值减少一个
            2. 每次遍历，当前果树的值 += 1
            3. k < 0 时，表示当前篮子装了第三种果树
               nums[i] 表示最先进入 sliding window 的果树类型，需要标成 0，并且恢复一个 sliding window 的额度 k += 1
               每次循环 i += 1 表示将左边的指针右移（因为最先进滑动窗口的果树位置也改变了）
            4. 当前滑动窗口所能达到的最大长度，就是子数组的最大长度
            '''
            i = ans = 0
            win = defaultdict(lambda: 0)
            for j in range(len(nums)):
                if win[nums[j]] == 0:
                    k -= 1
                win[nums[j]] += 1
                while k < 0:
                    win[nums[i]] -= 1
                    if win[nums[i]] == 0:
                        k += 1
                    i += 1
                ans = max(ans, j - i + 1)
            return ans

        return atMostK(2, tree)
