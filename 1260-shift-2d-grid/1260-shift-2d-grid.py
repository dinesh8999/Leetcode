class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0]*n for i in range(m)]
        k%=(m*n)
        for i in range(m):
            for j in range(n):
                index = i*n+j
                newIndex = (index+k) %(m*n)
                newRow = newIndex // n
                newCol = newIndex % n
                ans[newRow][newCol] = grid[i][j]
        return ans
        