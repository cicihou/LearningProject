class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        backtracking

        time complexity: O(S), S 是所有可行解的长度之和
        space complexity: O(target)，空间复杂度取决于递归的栈深度，最差情况下需要递归 target 层

        视频：https://www.youtube.com/watch?v=irFtGMLbf-s
        代码：https://leetcode-cn.com/problems/combination-sum/solution/zu-he-zong-he-by-leetcode-solution/
        '''
        res = []

        def dfs(target, combine, idx):
            if idx == len(candidates):
                return
            if target == 0:
                res.append(combine)
                return

            # 直接跳过，不用 cadidates[idx]
            dfs(target, combine, idx+1)

            # 选择当前数
            if target - candidates[idx] >= 0:
                dfs(target-candidates[idx], [*combine, candidates[idx]], idx)

        dfs(target, [], 0)
        return res


        '''
        method 2 
        prune + backtracking
        https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
        
        这个解法很实用，可以直接复用到第 40 题
        '''
        # 利用 sort prune, candidates 有序才能保证在 target -= candidates[i] 推出时，没有candidates[i] 后面的数 让 target 恰好等于 0
        candidates.sort()
        res = []
        def prune_dfs(begin, path, target):
            if target == 0:
                res.append(path)
                return
            for i in range(begin, len(candidates)):
                # 注意这里需要单独用一个变量 residue，若是用 target -= candidates[i] 在后面的循环中 target 的残值会变小
                residue = target - candidates[i]
                if target < 0:
                    break
                prune_dfs(i, [*path, candidates[i]], residue)

        path = []
        prune_dfs(0, path, target)
        return res


s = Solution()
s.combinationSum([2,3,6,7,4], 7)
