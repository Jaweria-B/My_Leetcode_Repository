class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * 50001
        
        for i in nums:
            freq[i] += 1
        
        res, operations = 0, 0
        
        for i in range(50000, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                res += operations - freq[i]
                
        return res