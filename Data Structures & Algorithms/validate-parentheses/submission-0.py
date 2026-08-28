class Solution:
    def isValid(self, s: str) -> bool:
        circel, square, curly = 0, 0, 0
        last = []
        for char in s:
            if char == '(':
                circel += 1
                last.append(')')
            elif char == '[':
                square += 1
                last.append(']')
            elif char == '{':
                curly += 1
                last.append('}')
            elif last == []:
                return False
            elif char == last[-1]:
                last.pop()
            elif char != last[-1]:
                return False
            
        return last == []