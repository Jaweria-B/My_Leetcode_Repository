class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        answer = 0
        n = len(nums)
        if n == 1 or n == 0:
            return answer
        
        for i in range(1, n):
            
            if nums[i] > nums[i-1]:
                continue
            
            num_of_oper = nums[i-1] - nums[i] + 1
            
            answer += num_of_oper 
            
            nums[i] = nums[i] + num_of_oper
            
        return answer