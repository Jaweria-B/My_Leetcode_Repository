class Solution:
    def canJump(self, nums: List[int]) -> bool:
        I=len(nums)-1
        if I == 0:
            return True
        for i in nums[-2::-1]:
            I -= 1
            L=len(nums)
            #print(L)
            if i+I>= L-1:
                nums = nums[0:I+1]
            #print(i,I,nums)
            if I == 0:
                #print(i,I,nums,L)
                if i >= L-1:
                    return True
                if i < L-1:
                    return False

                