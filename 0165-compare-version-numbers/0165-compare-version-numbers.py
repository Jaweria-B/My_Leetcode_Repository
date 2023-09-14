class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        length = min(len(v1), len(v2))
        
        for i in range(length):
            if int(v1[i]) == int(v2[i]):
                continue
        
            if int(v1[i]) < int(v2[i]):
                return -1
            
            if int(v1[i]) > int(v2[i]):
                return 1
        
        if len(v1) < len(v2):
            for i in range(length, len(v2)):
                if int(v2[i]) > 0:
                    return -1
                
        elif len(v1) > len(v2):
            for i in range(length, len(v1)):
                if int(v1[i]) > 0:
                    return 1
        
        return 0