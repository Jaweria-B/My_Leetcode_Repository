class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        rows = len(grid)
        cols = len(grid[0])
        modulo = rows * cols
        k = k % modulo
        
        if k == 0:
            return grid
        
        def swap_values(idx1, idx2):
            row1 = idx1 // cols
            col1 = idx1 % cols
            row2 = idx2 // cols
            col2 = idx2 % cols
            
            grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]
            
        idx = 0
        new_idx = 0
        elements_placed = 0
        
        while elements_placed < (modulo - 1):
            new_idx = (new_idx + k) % modulo
            
            if new_idx == idx:
                idx += 1
                new_idx = idx
                elements_placed += 1
                continue
                
            swap_values(idx, new_idx)
            elements_placed += 1
            
        return grid