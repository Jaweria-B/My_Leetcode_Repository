class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = defaultdict(int)
        
        for i in nums:
            dic[i] += 1
        
        output = []
        
        while dic:
            arr = []
            to_del = []
            
            for key, val in dic.items():
                                  
                arr.append(key)
                val -= 1
                
                dic[key] = val
                
                if val == 0:
                    to_del.append(key)
                    
                    
            output.append(arr)
            
            for key in to_del:
                    del dic[key]
            
            
        return output