class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])
        orig = image[sr][sc]

        if orig == newColor:
            return image

        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and image[x][y] == orig:
                image[x][y] = newColor
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        dfs(sr, sc)
        return image
