class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        global ans
        ans = []
        nums = [1,2,3,4,5,6,7,8,9]
        def calculate(nums, k, n, path, ind):
            global ans
            if k < 0 or n < 0:
                return
            
            if n == 0 and k == 0:
                ans.append(path[:])
                return
            
            for i in range(ind, len(nums)):
                path.append(nums[i])
                calculate(nums, k-1, n-nums[i], path, i+1)
                path.pop()
                
        calculate(nums, k, n, [], 0)
        
        return ans