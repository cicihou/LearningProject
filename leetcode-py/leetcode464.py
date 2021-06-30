class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        '''
        method 1
        Brute Force，TLE

        acc 表示当前累计的数字和

            dfs(acc) 就表示当传入一个当前的和时，己方会不会赢
                如果当前的 acc 已经 >= target，那么 P1 无法再加数，游戏已经在上一轮结束了，代表对方处于赢的状态
                如果当前的 acc 尚未到达 target，那么就进行 P1 可选择的数的穷举，并在此基础上进行 P2 的穷举
                    dfs(acc + n) 就表示当前的数是在以 P1 选择了的数之后的基础上，P2 再次穷举之后可进行的选择
                    （e.g. 共有 10 个数，P1 选了一个之后，P2 也可以再选 10 个数（此时的 dfs 函数 先手是 P2）
                    只要当前 acc 没有超过 target，状态空间树（state space tree）就可以不断向下选择，直到有确定的返回为止
        这种方法，允许重复选择数字，但我们实际问题中，没有必要重复选择
        实质上，由于 P1 是先手，所以 P1 在回溯所有答案时，只要能够得到一个让自己赢的数字方案，就必然会选择这条路径
        （it seems like the Doctor Strange in the Avengers XD）
        根据这个思想，我们可以进行状态压缩

        这一题比较抽象，理解上需要画图(实在理解不了就算了，尽力吧)
        '''
        def dfs(acc):
            if acc >= desiredTotal:
                return False
            for n in range(1, maxChoosableInteger + 1):
                # 如果对方有一种情况赢不了，那挑选这个数字就赢了，返回 True，代表可以赢
                if not dfs(acc + n):
                    return True
            return False
        return dfs(0)


        '''
        method 2 状态压缩
        由 method 1 演化而来，用 set 记录已经进行过的选择
        
        对两种我们已经确定的状态进行剪枝 prune
            1. 如果 target < maxChoosableInteger, P1 先手只需要选最大的那个数字就能赢，所以 P1 稳赢
            2. 如果 可以选择的所有数字加起来都 < target，那么 P1 P2 选择完所有的数字，游戏结束，都没有人能赢，所以 P1 会输（not 赢）
        
        剩下的 backtrack 思想整体跟 method 1 一致，只是加入了状态压缩的思想
        （所有的数字不可重复选，用 set() 记录，注意 backtracking 中需要进行状态撤销）
        
        tips:
        backtrack 无需记录当前是 P1 还是 P2，只需要返回当前用户的输赢就好
        我们从 P1 开始，当前得到的答案自然是 P1 的输赢
        也可以用 len(picked) % 2 == 0 来判断当前是 P1 还是 P2，打印出来，帮助理解
        
        TLE
        '''
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        def backtrack(picked, acc):
            # 传入的数已经超过 target，表示当前的 player 稳输
            if acc >= desiredTotal:
                return False

            # 当前所有的数都被选了，还没有赢，也表示当前的 player 输
            if len(picked) == maxChoosableInteger:
                return False

            for n in range(1, maxChoosableInteger + 1):
                if n not in picked:
                    picked.add(n)
                    # 对方有一种情况赢不了，我就选这个数字就能赢，返回 True, 代表可以赢
                    # 博弈时，两个 Player 都会选择对自己最优的解
                    if not backtrack(picked, acc+n):
                        picked.remove(n)
                        return True
                    picked.remove(n)
            return False
        return backtrack(set(), 0)


        '''
        上一种写法在 python3 也会超时
        
        method 3 使用位运算改进和优化（如果不使用 lru_cache 也是会超时的。。）
        lru_cache 的作用：https://stackoverflow.com/questions/49883177/how-does-lru-cache-from-functools-work
        '''
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        def dp(picked, acc):
            if acc >= desiredTotal:
                return False
            if picked == (1 << (maxChoosableInteger + 1)) - 1:
                return False
            for n in range(1, maxChoosableInteger + 1):
                if picked & 1 << n == 0:
                    if not dp(picked | 1 << n, acc + n):
                        return True
            return False

        return dp(0 ,0)
