class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        first = 0
        sec = 1
        
        count = 2
        
        while count != n+1:
            temp = first + sec
            first = sec
            sec = temp
            
            count += 1
        
        return temp