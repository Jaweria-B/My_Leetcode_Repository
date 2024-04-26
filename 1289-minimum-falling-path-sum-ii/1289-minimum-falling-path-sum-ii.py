class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Initialize a two-dimensional array to cache the result of each sub-problem
        memo = [[inf] * n for _ in range(n)]

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        next_min2_c = None
        
        # Base Case. Fill and save the minimum and second minimum column index
        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]
            if next_min1_c is None or memo[n - 1][col] <= memo[n - 1][next_min1_c]:
                next_min2_c = next_min1_c
                next_min1_c = col
            elif next_min2_c is None or memo[n - 1][col] <= memo[n - 1][next_min2_c]:
                next_min2_c = col
            
        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    memo[row][col] = grid[row][col] + memo[row + 1][next_min1_c]
                else:
                    memo[row][col] = grid[row][col] + memo[row + 1][next_min2_c]
                
                # Save minimum and second minimum column index
                if min1_c is None or memo[row][col] <= memo[row][min1_c]:
                    min2_c = min1_c
                    min1_c = col
                elif min2_c is None or memo[row][col] <= memo[row][min2_c]:
                    min2_c = col
            
            # Change of row. Update next_min1_c and next_min2_c
            next_min1_c = min1_c
            next_min2_c = min2_c
        
        # Return the minimum from the first row
        return memo[0][next_min1_c]