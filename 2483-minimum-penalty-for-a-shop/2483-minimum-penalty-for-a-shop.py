class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        currPenalty = minPenalty = customers.count('Y')
        earliestHour = 0
        
        for i, ch in enumerate(customers):
            
            if ch == 'Y':
                currPenalty -= 1
            else:
                currPenalty += 1
                
            
            if currPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = currPenalty
        
        return earliestHour