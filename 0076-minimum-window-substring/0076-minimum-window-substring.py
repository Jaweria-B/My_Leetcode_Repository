class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return (g:={'s':s,'t':t,'a':0,'c':Counter(),'d':Counter(t),'r':[inf,'']}) and \
            all([g.update({'b':b}),exec('c[s[b]]+=1',g),exec('while all(c[v]>=d[v] for v in d):r=min(r,[b-a+1,s[a:b+1]]);c[s[a]]-=1;a+=1',g)] for b in range(len(s))) and g['r'][1]