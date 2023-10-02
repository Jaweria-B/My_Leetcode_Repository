class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ind = 0
        count = 0
        
        for i in range(len(mat)):
            
            strength = sum(mat[i])
            if count < strength:
                count = strength
                ind = i
                
           
        return [ind, count]