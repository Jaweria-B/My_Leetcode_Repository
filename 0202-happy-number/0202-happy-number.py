class Solution:
    def isHappy(self, n: int) -> bool:
        n=str(n)
        ch=False
        if n=='1':
            ch=True
        else:
            while n not in ('2', '3', '4', '5', '6', '8','9'):
                s=0
                for i in n:
                    s+=int(i)**2
                if s==1:
                    ch=True
                    break
                else:
                    n=str(s)
        return ch