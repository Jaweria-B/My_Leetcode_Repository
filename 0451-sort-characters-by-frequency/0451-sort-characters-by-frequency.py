class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
            
        bucketList = defaultdict(list)
        
        for char, cnt in count.items():
            bucketList[cnt].append(char)
        
        res = []
        for i in range(len(s), 0, -1):
            for ch in bucketList[i]:
                res.append(ch * i)
        
        return "".join(res)