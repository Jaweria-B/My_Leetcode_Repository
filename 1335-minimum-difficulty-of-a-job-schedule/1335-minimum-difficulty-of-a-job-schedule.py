class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        #Check if can't find schedule
        if n < d: return -1
        #Precompute hardestjob array for index i and after
        curr_hardest = 0
        hardest_arr = [0] * (n)
        for i in range(n-1, -1, -1):
            curr_hardest = max(curr_hardest, jobDifficulty[i])
            hardest_arr[i] = curr_hardest
            
        #functools for memoization
        @lru_cache(maxsize=None)
        #Top-Down, state variables: i for index of jobDifficulty, day for current day
        def Memoization(i: int, day: int) -> int:
            #base case
            if day == d:
                return hardest_arr[i]
            #reccurence relation
            hardest = 0
            best = float('inf')
            for j in range(i, n-(d-day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + Memoization(j+1,day+1))
            return best
        return Memoization(0, 1)