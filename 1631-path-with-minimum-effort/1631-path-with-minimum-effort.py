class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows, cols = len(heights), len(heights[0])
        minHeap = [(0,0,0)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        costs = [[float("inf")]*cols for _ in range(rows)]
        costs[0][0] = 0
        
        while minHeap:
            cost, row, col = heappop(minHeap)
            visited.add((row, col))
            
            for direction in directions:
                r, c = row + direction[0], col + direction[1]
                
                if 0 <= r < rows and 0 <= c < cols and (r,c) not in visited:
                    neighbour_cost = max(cost, abs(heights[row][col] - heights[r][c]))

                    if neighbour_cost < costs[r][c]:
                        heappush(minHeap, (neighbour_cost, r, c))
                        costs[r][c] = neighbour_cost
                    
        return costs[rows-1][cols-1]