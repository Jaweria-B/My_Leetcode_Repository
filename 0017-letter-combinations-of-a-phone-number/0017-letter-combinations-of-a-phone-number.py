class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
     
        if digits == "":
            return []
        
        nums = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        ans = [""]
        
        for i in range(len(digits)):
            
            d = digits[i]
            temp = []
            
            for j in nums[d]:
                
                for k in range(len(ans)):
                    
                    temp.append(ans[k] + j)
                    
            ans = temp
            
        return ans 
        
        