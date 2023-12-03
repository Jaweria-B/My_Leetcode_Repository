class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            targ_x, targ_y = points[i + 1]
            
            total += max( abs(targ_x - curr_x), abs(targ_y - curr_y))
        
        return total
            