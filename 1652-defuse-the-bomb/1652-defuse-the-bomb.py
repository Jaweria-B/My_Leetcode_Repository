class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        else:
            output = []
            
            pos_K = abs(k)
            summ = sum(code[0 : pos_K])
            for i in range(len(code)):
                summ = summ - code[i] + code[(i+pos_K)%len(code)]
                output.append(summ)
            
            if k < 0:
                output = output[k-1 : ] + output[: k-1]
            
            return output