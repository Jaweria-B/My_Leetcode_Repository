class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        
        count = 0
        while factorial > 0:
            rem = factorial % 10
            if rem != 0:
                break
            count += 1
            
            factorial //= 10
            
        return count
            