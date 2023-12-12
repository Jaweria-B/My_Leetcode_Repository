class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maximum = float('-INF')
        sec_max = float('-INF')
        
        for i in nums:
            if i >= maximum:
                sec_max = maximum
                maximum = i
            elif i >= sec_max:
                sec_max = i
                
        return (maximum - 1) * (sec_max - 1)