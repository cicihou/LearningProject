class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        method1 DFS
        这个写法其实是对的（自己想的哦），但是 TLE
        '''
        self.seen = {(sx, sy)}

        def dfs(x, y):
            for nx, ny in [(x + y, y), (x, x + y)]:
                if (nx, ny) in self.seen:
                    continue
                if nx <= tx and ny <= ty:
                    self.seen.add((nx, ny))
                    dfs(nx, ny)

        dfs(sx, sy)
        return (tx, ty) in self.seen

        '''
        method 2 上面的从前往后会超时，试一下从后往前
        
        https://leetcode.com/problems/reaching-points/discuss/114856/JavaC%2B%2BPython-Modulo-from-the-End
        https://leetcode.com/problems/reaching-points/discuss/375429/Detailed-explanation.-or-full-through-process-or-Java-100-beat
        
        
        why could we use module?
        
        "ty = ty - tx" -> Take modulo on both sides , ty%tx = ty%tx -tx%tx  ==> ty%tx = ty%tx
        if we do ty=ty-tx , this way it can give TLE , but if we do ty=ty%tx , this way we will get to the answer very fast
        
        (ty - sy) % sx == 0  也就是说 targetY 和 sourceY 之间的差值可以通过不停的减去 sourceX来实现
        同理 (tx - sx) % sy == 0 就是 targetX 和 sourceX 之间的差值是 sourceY 的整数倍
        '''
        while sx < tx and sy < ty:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty

        return (sx == tx and sy <= ty and (ty - sy) % sx == 0) or (sy == ty and sx <= tx and (tx-sx) % sy == 0)
