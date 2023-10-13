class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        ans = 0
        
        for num in dic:
            if num+1 in dic:
                ans = max(ans, dic[num]+dic[num+1])
        
        return ans