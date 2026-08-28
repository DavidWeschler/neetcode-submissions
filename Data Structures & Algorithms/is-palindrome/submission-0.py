class Solution:
    def isPalindrome(self, s: str) -> bool:
        myString = re.sub(r'\s+', '', s)
        myString = re.sub(r'[^a-zA-z0-9]', '', s)
        myString = myString.lower()
        return myString == myString[::-1]