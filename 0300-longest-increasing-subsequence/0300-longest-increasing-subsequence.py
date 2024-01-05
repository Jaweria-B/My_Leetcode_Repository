class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[nums[0]]
        for x in nums[1:]:
            if x>lis[-1]:
                lis.append(x)
            else:
                i=bisect.bisect_left(lis, x)
                lis[i]=x
        return len(lis)
        