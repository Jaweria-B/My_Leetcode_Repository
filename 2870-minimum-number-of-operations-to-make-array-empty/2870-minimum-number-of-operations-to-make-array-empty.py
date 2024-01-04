class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        
        for i in nums:
            dic[i] += 1
        
        if min(dic.values()) == 1:
            return -1
        
        output = 0
        
        for num, count in dic.items():
            output += ceil(count/3)
        
        return output