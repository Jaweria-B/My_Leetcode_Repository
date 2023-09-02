class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dic = collections.Counter(changed)
        ans = []
        for ele in sorted(dic):
            if dic[ele] > dic[ele*2]:
                return []
            
            if ele == 0:
                if dic[ele]%2 != 0:
                    return []
                else:
                    ans += ([0]*(dic[ele]//2))
            else:
                dic[ele*2] -= dic[ele]
            
        
        for k, v in dic.items():
            if k != 0:
                ans += [k]*v
        #print(ans)
        return ans