class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        根据 39 的 solution 2 改的，多加了一些剪枝的手段

        也可参考，https://leetcode.com/problems/combination-sum-ii/solution/，去重和剪枝方式略有不同（通过比较 continue 了一次循环）

        例如一个 candidates = [1,1,2,5]，target = 8，由于题目要求元素不能重复使用
        虽然在 [c[0], c[2], c[3]] 和 [c[1], c[2], c[3]] 在我们看来是不同的组合，但其实反映在结果集中只对应一个答案
        因此我们用 set[tuple[int]] 这个结构去重
        '''
        res = set()
        candidates.sort()

        def dfs(start, target, path):
            if target == 0:
                res.add(tuple(path))
                return
            if sum(candidates[start:]) < target:
                # prune: 当一个 dfs 进行时，candidates 后面剩余的数加起来都没 target 大，退出递归
                return
            for i in range(start, len(candidates)):
                residue = target - candidates[i]

                # prune: 当循环进行时的残值 < 0，由于 candidates 有序，后面不存在有用的数
                if residue < 0:
                    break
                # 这里唯一跟 39 题不同的就是，进入递归的时候需要 i+1，因为当前的数在结果集中不可重复使用
                dfs(i+1, residue, path+candidates[i])

        path = []
        dfs(0, target, path)
        return res
