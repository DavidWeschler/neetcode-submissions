class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        chars = {}

        for right in range(len(s)):
            if s[right] in chars and chars[s[right]] >= left:
                left = chars[s[right]] + 1
            
            chars[s[right]] = right
            maxLen = max(maxLen, right-left+1)

        return maxLen