class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = j = 1
        while i < len(arr) - 1 and arr[i-1] < arr[i]:
            i += 1
        while j < len(arr) - 1 and arr[len(arr)-j] < arr[len(arr)-j-1]:
            j += 1
        return i == len(arr) - j + 1
