class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = defaultdict()  # the projection dict, key is the char in pattern and the value is a word
        words = s.split(' ')
		# 'aa' -> 'dog', 'ab' -> 'dog dog', 'abc'- > 'cat dog cat'
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)): return False
        for i, c in enumerate(pattern):
            if c in dic:  # c has been projected to some word
                if dic[c] != words[i]: return False  # 'aba' -> 'cat dog dog'
            else:
                dic[c] = words[i]
        return True
            
        