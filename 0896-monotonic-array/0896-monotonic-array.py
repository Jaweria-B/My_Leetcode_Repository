class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums==(t:=sorted(nums))or nums==t[::-1]