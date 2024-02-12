class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        count = Counter(nums)
        
        for num, cnt in count.items():
            if cnt >= n / 2:
                return num