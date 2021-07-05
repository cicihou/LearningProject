class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        每个小孩都会用掉一块饼干，因此先排序，优先用 s[i] 值小 的饼干 满足 g[i] 值小的宝贝

        当 s[i] >= g[i] 值，这个宝贝可以用这块饼干满足，小朋友满足 + 1，饼干消耗 + 1
        当 s[i] <  g[i] 值，这个宝贝不能用这块饼干满足（无用的小饼干），饼干废弃 + 1，小朋友满足数量无变化

        返回最后被满足的小朋友数量

        time: O(nlogN)
        space: O(1)
        '''
        g.sort()
        s.sort()
        pg = 0
        ps = 0
        while pg < len(g) and ps < len(s):
            if s[ps] >= g[pg]:
                pg += 1
                ps += 1
            else:
                ps += 1
        return pg
