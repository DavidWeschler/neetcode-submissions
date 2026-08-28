class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
    
        if len(s) != len(t):
            return False
        
        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

        for l in s_hash.keys():
            if l not in t_hash.keys() or s_hash[l] != t_hash[l]:
            # if s_hash[l] != t_hash.get(l, 0):
                return False
        
        return True