class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        res = ROWS * 2** (COLS - 1)
        
        for c in range(1, COLS):
            cnt = 0
            for r in range(ROWS):
                if grid[r][c] == grid[r][0]:
                    cnt += 1
            cnt = max(cnt, ROWS - cnt)
            res += cnt * 2** (COLS - c - 1)
            
        return res
                    