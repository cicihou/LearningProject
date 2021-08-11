class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        '''
        用了一点数学的特性，还是挺巧妙的
        arr 可以任意重组，因此我们只需要判断arr 中的元素个数即可
        按绝对值排序，直接统计个数，不需要再纠结正数用乘法，负数用除法

        :param arr:
        :return:
        '''
        counter = Counter(arr)
        for x in sorted(arr, key=abs):
            if counter[x] == 0:
                continue
            if counter[2*x] == 0:
                return False
            counter[x] -= 1
            counter[2*x] -= 1
        return True
