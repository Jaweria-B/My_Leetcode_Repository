class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGain = 0
        currentGain = 0
        answer = 0
        
        for i in range(len(gas)):
            
            totalGain += gas[i] - cost[i]
            currentGain += gas[i] - cost[i]
            
            if currentGain < 0:
                currentGain = 0
                answer = i + 1
                
        return answer if totalGain >= 0 else -1