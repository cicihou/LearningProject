class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = arr[:]
        arr = list(set(arr))
        arr.sort()
        rank = {arr[i]:i+1 for i in range(len(arr))}
        res = [rank[num] for num in nums]
        return res
