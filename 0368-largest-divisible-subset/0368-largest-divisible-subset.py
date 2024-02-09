class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}
        
        def dfs(i, prev):
            if i == len(nums):
                return []
            
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            res = dfs(i + 1, prev)
            
            if nums[i] % prev == 0:
                tmp = [nums[i]] + dfs(i + 1, nums[i])
                res = tmp if len(tmp) > len(res) else res
            
            cache[(i, prev)] = res
            return res
        
        return dfs(0, 1)