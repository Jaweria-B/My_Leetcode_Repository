class Solution:
    def grayCode(self, n: int) -> List[int]:
        def calculate(n):
            
            if n == 1:
                return ["0", "1"]
            
            temp = calculate(n-1)
            ans = []
            
            for i in range(len(temp)):
                ans.append("0" + temp[i])
            
            for i in range(len(temp)-1, -1, -1):
                ans.append("1" + temp[i])
                
            return ans
            
        combinations = calculate(n)
        
        ans = []
        for comb in combinations:
            ans.append(int(comb, 2))
        
        return ans
    
        