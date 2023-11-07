class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        prefixSum = 0
        
        dic = {}
        dic[0] =  1
       
        for i in nums:
            
            prefixSum += i
            
            if prefixSum-k in dic:
                ans += dic[prefixSum - k]
            
            dic[prefixSum] = dic.get(prefixSum, 0) + 1
            
        return ans