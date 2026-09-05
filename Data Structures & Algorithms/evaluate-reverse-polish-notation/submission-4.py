class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for s in tokens:
            if self.is_integer(s):
                stack.append(int(s))
            else:
                second = stack.pop()
                first = stack.pop()
                if s == '+':
                    stack.append(first + second)
                elif s == '-':
                    stack.append(first - second)
                elif s == '*':
                    stack.append(first * second)
                elif s == '/':
                    stack.append(int(first / second))
        return stack.pop()
        
    def is_integer(self, string_to_check):
        try:
            int(string_to_check)
            return True
        except ValueError:
            return False