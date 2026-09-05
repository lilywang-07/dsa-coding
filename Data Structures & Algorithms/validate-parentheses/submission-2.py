class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', ']':'[','}':'{'}
        stack = deque()
        for char in s:
            if char in match.values(): # open
                stack.append(char)
            elif stack and match[char] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True