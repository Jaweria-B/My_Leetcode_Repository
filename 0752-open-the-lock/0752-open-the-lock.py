class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
                
        if  "0000" in visited:
            return -1

        def getNextLevelCombinations(password):
            output = []
            for i in range(4):
                num = int(password[i])
                for j in [-1,1]:
                    next_val = (num+j)%10
                    next_password = password[0:i] + str(next_val) + password[i+1:]
                    output.append(next_password)
            return output
        
        queue = collections.deque([("0000", 0)])
        
        while queue:
            password, steps = queue.popleft()
            
            if password == target:
                return steps
            
            for next_level in getNextLevelCombinations(password):
                if next_level not in visited:
                    visited.add(next_level)
                    queue.append([next_level, steps+1])
        
        return -1