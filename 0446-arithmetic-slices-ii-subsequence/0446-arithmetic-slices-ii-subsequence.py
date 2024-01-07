class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [ defaultdict(int) for _ in range(n) ]
        
        total = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total += dp[j][diff]
        
        return total