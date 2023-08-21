class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        
        def calculate(row, col, memo):
            
            if (row, col) in memo:
                return memo[(row,col)]
            
            if row == len(triangle)-1:
                return triangle[row][col]
            
            memo[(row,col)] = triangle[row][col] + min(calculate(row+1, col, memo), calculate(row+1, col+1, memo))
            
            return memo[(row,col)]
        
        return calculate(0, 0, memo)