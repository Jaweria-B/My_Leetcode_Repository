class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        clockwise_distance = 0
        n = len(distance)
        i = start
        
        while i != destination:
            clockwise_distance += distance[i]
            start += 1
            i = start % n
        
        anticlockwise_distance = sum(distance) - clockwise_distance
        
        return min(clockwise_distance, anticlockwise_distance)