class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        splitted = sentence.split(" ")
        
        if len(splitted) == 1:
            return splitted[0][0] == splitted[-1][-1]
        
        else:
            for i in range(len(splitted)-1):
                if splitted[i][-1] != splitted[i+1][0]:
                    return False
                
            return True and splitted[0][0] == splitted[-1][-1]