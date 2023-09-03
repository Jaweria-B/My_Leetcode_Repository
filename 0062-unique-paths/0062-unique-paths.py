class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def paths(i, j, m, n, dp):
            
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = paths(i+1, j, m, n, dp) + paths(i, j+1, m, n, dp)
            
            return dp[i][j] 
    
        dp = [[-1]*n for _ in range(m)]
        return paths(0, 0, m, n, dp)