class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         HashSet 

        n = len(nums)
        hashSet = set()
        
        for i in range(n):
            if nums[i] in hashSet: return nums[i]
            else: hashSet.add(nums[i])
        
        return n