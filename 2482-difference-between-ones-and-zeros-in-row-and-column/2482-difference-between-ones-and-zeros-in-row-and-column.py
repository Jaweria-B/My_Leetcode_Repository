class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        zerosRow = []
        onesCol = []
        zerosCol = []
        
        for r in grid:
            count_1s = r.count(1)
            count_0s = len(r) - count_1s
            onesRow.append(count_1s)
            zerosRow.append(count_0s)
                    
        for i in range(len(grid[0])):
            count_1s = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    count_1s += 1
            
            count_0s = len(grid) - count_1s
            onesCol.append(count_1s)
            zerosCol.append(count_0s)
        
        ans = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                ans[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

        return ans