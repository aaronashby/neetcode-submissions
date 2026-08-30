class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                brackets.append(c)
            elif len(brackets) > 0:
                if c == ')' and brackets[-1] == '(':
                    brackets.pop()
                elif c == ']' and brackets[-1] == '[':
                    brackets.pop()
                elif c == '}' and brackets[-1] == '{':
                    brackets.pop()
                else:
                    return False
            else:
                return False
        return len(brackets) == 0