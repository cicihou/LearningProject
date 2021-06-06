from collections import defaultdict, Counter


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
        exactK = atMostK(k) - atMostK(k-1)

        这个问题跟 904 一模一样，不过 904 只要最大，这个是累计
        '''

        def atMostK(arr, k):
            ans = i = 0

            # 这两个结构，在这里达到的效果都是一致的，都是为了给 key 赋默认值 0
            # subarray = defaultdict(lambda: 0)
            subarray = Counter()

            for j in range(len(arr)):
                if subarray[arr[j]] == 0:
                    k -= 1
                subarray[arr[j]] += 1
                while k < 0:
                    subarray[arr[i]] -= 1
                    if subarray[arr[i]] == 0:
                        k += 1
                    i += 1
                ans += j - i + 1
            return ans

        return atMostK(nums, k) - atMostK(nums, k - 1)
