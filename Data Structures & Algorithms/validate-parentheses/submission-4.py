class Solution:
    def isValid(self, s: str) -> bool:
        openParentheses = ["(", "[", "{"]
        closeParentheses = [")", "]", "}"]
        stack = []

        for c in s:
            if c in openParentheses:
                stack.insert(0, c)
            else:
                if len(stack) == 0:
                    return False
                opener = stack.pop(0)

                if c == ")":
                    if opener != "(":
                        return False
                if c == "]":
                    if opener != "[":
                        return False
                if c == "}":
                    if opener != "{":
                        return False
                        
        return len(stack) == 0