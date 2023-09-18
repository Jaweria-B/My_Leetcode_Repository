class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            strength = sum(row)
            heapq.heappush(heap, (-strength, -i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [-i for _, i in sorted(heap, reverse=True)]