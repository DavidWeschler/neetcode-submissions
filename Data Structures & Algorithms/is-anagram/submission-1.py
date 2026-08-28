class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1
        
        for char in s_chars:
            if s_chars.get(char, 0) != t_chars.get(char, 0):
                return False    

        for char in t_chars:
            if t_chars.get(char, 0) != s_chars.get(char, 0):
                return False
        
        return True