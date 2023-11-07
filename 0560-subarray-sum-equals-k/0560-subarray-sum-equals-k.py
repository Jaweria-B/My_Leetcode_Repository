class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        dic = {}
        dic[0] =  1
        
        preSum = [nums[0]]
        
        for i in nums[1:]:
            preSum.append(i+ preSum[-1])
        
        for i in preSum:
            
            if i-k in dic:
                ans += dic[i-k]
            
            dic[i] = dic.get(i, 0) + 1
            
        return ans