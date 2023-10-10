class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum  =sum(nums)
        
        def digit_sum(nums):
            dig_sum = 0
            
            for i in range(len(nums)):
                num = nums[i]
                while num > 0:
                    rem = num%10
                    dig_sum += rem
                    num = num//10
            
            return dig_sum
        
        dig_sum = digit_sum(nums)
        
        return abs(ele_sum - dig_sum)