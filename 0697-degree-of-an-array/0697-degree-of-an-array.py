class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        degree = max(dic.values())
        
        l = {}
        r = {}
        
        for i in range(len(nums)):
            if nums[i] not in l:
                l[nums[i]] = i
                
            r[nums[i]] = i
        
        ans = float("inf")
        
        for num in dic:
            if dic[num] == degree:
                ans = min(ans, r[num]-l[num]+1)
        
        return ans