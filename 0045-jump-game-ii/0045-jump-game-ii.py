class Solution:
    def jump(self, nums: List[int]) -> int:
        i = max_reachable = curr_reachable = jumps = 0
        n = len(nums)
        while i < n -1:
            max_reachable = max(max_reachable, i + nums[i])
            if i == curr_reachable:
                curr_reachable = max_reachable
                jumps += 1
            i += 1
    
        return jumps