class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(arr):
            arr.sort()
            
            diff = arr[1] - arr[0]
            
            for i in range(2, len(arr)):
                
                if arr[i] - arr[i-1] != diff:
                    return False
                
            return True
                
        ans = []
        m = len(l)
        
        for i in range(m):
            ans.append( check(nums[ l[i] : r[i] + 1 ]) )
        
        return ans