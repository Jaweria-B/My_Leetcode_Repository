class Solution:
    def myPow(self, x: float, n: int) -> float:
        rec = False
        if n < 0:
            rec = True
            n = -1*n
            
        if n == 0 :
            return 1
        
        ans = 1
        while n > 0:
            if n % 2 == 0:
                x = x * x
                n /= 2
            else:
                ans *= x
                n -= 1
            
        if rec == True:
            return 1 / ans
        else:
            return ans


