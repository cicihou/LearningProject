class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        linear sorted
        time O(N*log(N))
        space O(N)
        To build sortedArr, we need to sort every element in the array by a new criteria: x - num. This costs O(N⋅log(N))
        '''
        nums = sorted(arr, key=lambda a:abs(a-x))
        res = []
        for i in range(k):
            res.append(nums[i])
        return sorted(res)


        '''
        binary search + sliding window
        https://leetcode.com/problems/find-k-closest-elements/solution/
        找最靠近某个值 x 的 k 个数
        假设这个要找的值就是 x，那么 x 必定会是我们要找的数组所对应的坐标轴上，要找的那段值的中点
        如果 x 左边的边界点和右边的边界点相同了，优先取左，视同 [) 左闭右开
        那么，我们可以近似得知 x - arr[mid] > arr[mid + k] - x 最先满足这一条件的 left 值，就是我们要找的数
        
        （arr[mid], x, arr[mid+k]）这三个数在坐标点的大小关系如顺序，mid 到 mid + k 正好是 k 个数字
        不断向右侧靠近，left 和 mid 逼近，找到最快满足的左边界

        理解起来比较费劲
        '''
        l = 0
        r = len(arr) - k

        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]
