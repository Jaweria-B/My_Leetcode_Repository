class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        memo = [[[-1 for _ in range(maxMove+1)] for _ in range(n)] for _ in range(m)]
        def dfs(curr_r, curr_c, moves):
            if curr_r < 0 or curr_c < 0 or curr_c >= n or curr_r >= m: 
                return 1
            
            if moves == 0:
                return 0
            
            if memo[curr_r][curr_c][moves] != -1:
                return memo[curr_r][curr_c][moves]
    
            bottom = dfs(curr_r+1, curr_c, moves-1)
            top = dfs(curr_r-1, curr_c, moves-1)
            right = dfs(curr_r, curr_c+1, moves-1)
            left = dfs(curr_r, curr_c-1, moves-1)
            
            memo[curr_r][curr_c][moves] = bottom + top + right + left
            
            return memo[curr_r][curr_c][moves]
        
        return dfs(startRow, startColumn, maxMove)%MOD
        