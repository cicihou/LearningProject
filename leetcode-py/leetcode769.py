class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        题目给定一个长度为 n，里面值有且只有 [0, n-1] 的 arr
        要求将其分割成最多的块之后，块排序的结果是升序的

        思路解释：https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/138844/Python-O(n)-Very-Detailed-Explanation
        Since the array consists of elements from [0, N-1], for any value in the array, the corresponding index is where that element must end up in the end

        我们遍历整个 arr，若当前 trunk 的 max_value 跟我们当前遍历的 index 相等，说明当前有一个 trunk 可以独立出来，整体有序（i.e. 内部的元素是无序的，但这个 trunk 从整体来看包含的元素是有序的）

        这道题可以这样做是因为元素不会重复，768 就没办法直接这样判断了
        :param arr:
        :return:
        '''
        res = max_value = 0
        for i in range(len(arr)):
            max_value = max(max_value, arr[i])
            if max_value == i:
                res += 1
        return res
