class Solution:
    def splitNum(self, num: int) -> int:
        num = str(num)
        
        sorted_num = sorted(num)
        
        
        num1 = ""
        num2 = ""
        
        if len(num)%2 != 0:
            sorted_num = ["0"] + sorted_num
        
        for i in range(len(sorted_num)):
            if i%2 == 0:
                num1 += sorted_num[i]
            else:
                num2 += sorted_num[i]
        
        return int(num1) + int(num2)