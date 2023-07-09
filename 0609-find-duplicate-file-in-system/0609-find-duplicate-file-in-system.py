class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for directory in paths:
            splitted = directory.split(" ")
            
            for i in range(1, len(splitted)):
                file, content = splitted[i].split("(")
                #print(file, content)
                
                if content in dic:
                    dic[content].append(splitted[0] + "/" + file)
                else:
                    dic[content] = [splitted[0] + "/" + file]
        
        ans = []
        for key in dic:
            if len(dic[key]) > 1:
                ans.append(dic[key])
        
        return ans
        