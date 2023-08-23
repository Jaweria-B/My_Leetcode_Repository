class Solution:
    def reorganizeString(self, s: str) -> str:
#       making a dictionary
        dic = {}
#       storing the count of each character in the dictionary 
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
#       making a list so we can store all the characters along with their count 
        ch_cnt = []
#       placing the value variable first because we're gonna sort it
        for k, val in dic.items():
            ch_cnt.append((val, k))
#       sorting the list to get the most frequent character at left
        ch_cnt.sort()
        
#       making a list instead of a string variable as we're gonna place characters seperately using list as a grid
        ans = [0] * len(s)
#       if even the last character in list has more frequency than half of the list than it won't be possible to make a combination
        if ch_cnt[-1][0] > (len(s)+1)//2:
            return ""
#       placing the designated popped character with a space of 1 index on the grid 
        i = 0
        while ch_cnt:
            cnt, ch = ch_cnt.pop()
            
            while cnt != 0:
                ans[i] = ch
                cnt -= 1
                i += 2
                if i >= len(s):
                    i = 1
#       every index on ans array will be filled as its length is same as that of string

#       returning the answer as a string not as list/grid
        return "".join(ans)