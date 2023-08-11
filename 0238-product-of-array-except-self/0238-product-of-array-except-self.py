class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        leftProduct = [1] * n
        rightProduct = [1] * n
        
        for i in range(1, n):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
            
        for i in range(n-2, -1, -1):
            rightProduct[i] = rightProduct[i+1] * nums[i+1]
            
        result = [ leftProduct[i]* rightProduct[i] for i in range(n)]
        
        return result