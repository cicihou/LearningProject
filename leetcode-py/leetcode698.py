class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        '''
        这里其实跟 464 有点微妙的相似，我们只需要把各个情况对应的 bool值直接返回
        backtrack 的核心就是，遍历所有的值（可能性），找到有没有最终可以正确返回的结果
        如果当前的分支不是可行的解，那么 backtrack的核心就在我们会把此次的解法复原

        这个 naive backtrack 居然会超时

        time: O(N * N!)
        space: O(N)
        '''
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        n = len(nums)
        taken = [False] * n

        def backtrack(count, curr_sum):
            if count == k - 1:
                return True
            if curr_sum > target:
                return False
            if curr_sum == target:
                return backtrack(count + 1, 0)

            for j in range(n):
                if not taken[j]:
                    taken[j] = True
                    if backtrack(count, curr_sum + nums[j]):
                        return True
                    taken[j] = False
            return False

        return backtrack(0, 0)

        '''
        optimized backtrack
        
        先排序，使数组内元素有序
        记录一下backtrack 当前的位置，（由于有序）不可能的结果就不要再重复计算了
        
        time: O(k * 2 ^ N)
        space: O(N)
        '''
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        taken = [False] * n

        def backtrack(index, count, curr_sum):
            if count == k - 1:
                return True
            if curr_sum > target:
                return False
            if target == curr_sum:
                return backtrack(0, count + 1, 0)

            for i in range(index, n):
                if not taken[i]:
                    taken[i] = True
                    if backtrack(i + 1, count, curr_sum + nums[i]):
                        return True
                    taken[i] = False
            return False

        return backtrack(0, 0, 0)
