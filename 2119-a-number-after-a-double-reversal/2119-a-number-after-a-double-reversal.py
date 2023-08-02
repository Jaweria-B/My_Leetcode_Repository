class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if(len(str(num))==1):
            return True
        if(str(num)[-1]==0):
            return False
        r_int1 = int(str(num)[::-1])
        print(r_int1)
        r_int2 = int(str(r_int1)[::-1])
        if(r_int2==num):
            return True