class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for n in nums[:]:
            if n == val:
                nums.remove(n)
            else:
                count += 1
        return count
