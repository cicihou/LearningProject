class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        method 1 DFS

        time: O(n^2)，需要遍历矩阵的每个元素
        space: O(n)，用 visited 记录是否被访问过，visited 长度最多为 n ，递归调用栈的深度也不会超过 n

        跟 lc 200 有相似之处，根据一个点开始遍历其周边的点，矩阵虽然是 n*n 但是记录的无非也就是 n 个城市之间的关系

        i.e. isConnected[0][1] = 1 和 isConnected[1][0] = 1 其实是等价的，都是表示城市0 和城市1 之间连通

        因此我们每次找到城市之间的连通，就可以以当前城市为支点，搜寻其他城市
        （这个搜寻只需要进行 O(n) 的遍历，因为 matrix[0][1] 和 matrix[1][0] 的状态是等价的）
        也正因此，我们的 visited 只需要记录某个点的城市搜索状态即可
        如果某个城市被搜索过，后面就不需要再搜索这个城市和其相关的城市（认为是之前搜索过的同一个城市群）
        只有当碰到没有访问过的城市群时，再进行一次搜索和遍历
        '''
        provinces = len(isConnected)
        visited = set()
        circles = 0

        def dfs(i):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
        return circles

        '''
        method 2 BFS
        '''
        provinces = len(isConnected)
        visited = set()
        circles = 0
        for i in range(provinces):
            if i not in visited:
                q = collections.deque([i])
                while q:
                    j = q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if k not in visited and isConnected[j][k] == 1:
                            q.append(k)
                circles += 1
        return circles

        '''
        method 3 Union Find
        '''
        # TODO
