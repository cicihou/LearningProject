class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        '''
        time: O(n)
        space: O(n)

        这题有点意思

        :param pid:
        :param ppid:
        :param kill:
        :return:
        '''
        cache = {}
        for child, parent in zip(pid, ppid):
            if parent != 0:
                cache.setdefault(parent, []).append(child)
        self.res = []

        def dfs(k):
            if k in cache and cache[k]:
                values = cache.pop(k)
                self.res += values
                for kk in values:
                    dfs(kk)

        self.res.append(kill)
        dfs(kill)
        return self.res
