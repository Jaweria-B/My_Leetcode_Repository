class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        cache = {}
        
        def dfs(curr_r, curr_c, moves):
            
            if (curr_r == m or curr_r == -1 or curr_c == n or curr_c == -1) and moves >= 0:
                return 1
            
            if moves == 0:
                return 0
            
            if (curr_r, curr_c, moves) in cache:
                return cache[(curr_r, curr_c, moves)]
            
            bottom = dfs(curr_r + 1, curr_c, moves - 1)
            top = dfs(curr_r - 1, curr_c, moves - 1)
            right = dfs(curr_r, curr_c + 1, moves - 1)
            left = dfs(curr_r, curr_c - 1, moves - 1)
            
            cache[(curr_r, curr_c, moves)] = (top + bottom + right + left) % MOD
            
            return cache[(curr_r, curr_c, moves)]
        
        return dfs(startRow, startColumn, maxMove) % MOD