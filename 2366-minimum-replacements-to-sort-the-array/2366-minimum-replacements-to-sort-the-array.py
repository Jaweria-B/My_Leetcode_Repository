class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        answer = 0
        n = len(nums)
        
        for i in range(n-2, -1, -1):
            
            if nums[i] <= nums[i+1]:
                continue
            
            num_of_elements = (nums[i] + nums[i+1] - 1) // nums[i+1]
            
            answer += num_of_elements -1
            
            nums[i] = nums[i] // num_of_elements
        
        return answer