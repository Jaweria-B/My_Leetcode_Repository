class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(arr):
            Min = min(arr)
            Max = max(arr)
            
            if (Max - Min) % (len(arr) - 1) != 0:
                return False
            
            diff = (Max - Min) // (len(arr) - 1)
            
            
            arr_set = set(arr)
            curr = Min
            
            while curr < Max:
                
                if curr not in arr_set:
                    return False
                curr += diff
            
            return True
           
            
        ans = []
        m = len(l)
        
        for i in range(m):
            ans.append( check(nums[ l[i] : r[i] + 1 ]) )
        
        return ans