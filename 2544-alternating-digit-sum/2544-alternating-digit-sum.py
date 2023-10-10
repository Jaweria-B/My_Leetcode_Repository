class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        
        ans = 0
        
        
        for i in range(len(n)):
            if i%2 == 0:
                ans += int(n[i])
            else:
                ans += (-1*int(n[i]))
            
        return ans