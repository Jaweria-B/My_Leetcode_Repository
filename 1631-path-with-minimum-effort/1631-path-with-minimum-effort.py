class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        min_heap = [(0, 0, 0)]
        
        while min_heap:
            effort, x, y = heappop(min_heap)
            
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heappush(min_heap, (new_effort, nx, ny))
        
        return dist[rows-1][cols-1]