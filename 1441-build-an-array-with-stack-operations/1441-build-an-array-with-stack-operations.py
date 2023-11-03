class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        operations = []
        currNum = 1
        index = 0
        
        while currNum <= n and index < len(target):
            num = target[index]
            
            if num == currNum:
                operations.append("Push")
                currNum += 1
                index += 1
            else:
                operations.append("Push")
                operations.append("Pop")
                currNum += 1
            
        return operations