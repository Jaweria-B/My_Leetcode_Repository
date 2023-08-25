class Solution:
    def fib(self, n: int) -> int:
        
        def find(n, memo):
            if n == 0 or n == 1:
                return n
            
            if memo[n] != -1:
                return memo[n]
            
            memo[n] = find(n-1, memo) + find(n-2, memo)
            
            return memo[n]
        
        memo = [-1] * (n+1)
        
        return find(n, memo)