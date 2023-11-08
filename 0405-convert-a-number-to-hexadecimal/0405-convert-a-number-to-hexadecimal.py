class Solution:
    def toHex(self, num: int) -> str:
        dic = {10 : "a", 11 : "b", 12 : "c", 13 :"d", 14 : "e", 15: "f"}
        
        def conversion(num):
            ans = ""
            while num >= 16:
                rem = num%16
                if rem >= 10:
                    ans = str(dic[rem]) + ans
                else:
                    ans = str(rem) + ans
                
                num = num//16
            
            if num > 0:
                if num >= 10:
                    ans = str(dic[num])+ ans
                else:
                    ans = str(num)+ ans
                    
            return ans
        
        if num == 0:
            return "0"
        
        if num < 0:
            temp = 0xffffffff
            num = (temp^abs(num)) + 1
            
        return conversion(num)