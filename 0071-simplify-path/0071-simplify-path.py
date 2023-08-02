class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        i = 0
        while i < len(path):
            if path[i] == "/": 
                i += 1
                continue
                
            directory = ""
            while (i<len(path) and path[i] != "/"):
                directory += path[i]
                i += 1
            
            if directory == ".":
                continue
            
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
            
        
        return "/" + "/".join(stack)