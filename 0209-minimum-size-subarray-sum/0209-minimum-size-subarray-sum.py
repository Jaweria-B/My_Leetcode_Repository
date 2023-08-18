class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ans = float('inf')
        
        left = 0
        sm = 0
        
        for i in range(n):
            sm += nums[i]
            
            while sm >= target:
                ans = min(ans, (i+1-left))
                sm -= nums[left]
                left += 1
        
        return ans if ans!= float('inf') else 0