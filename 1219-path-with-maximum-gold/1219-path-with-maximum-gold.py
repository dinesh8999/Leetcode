class Solution:
    def getMaximumGold(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (1, 0),   
            (-1, 0),  
            (0, 1),   
            (0, -1)  
        ]

        def backtrack(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            
            if grid[r][c] == 0:
                return 0

            
            gold = grid[r][c]
            grid[r][c] = 0       

            max_gold = 0

            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                max_gold = max(
                    max_gold,
                    backtrack(nr, nc)
                )

           
            grid[r][c] = gold

            return gold + max_gold

        answer = 0

       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    answer = max(answer, backtrack(r, c))

        return answer