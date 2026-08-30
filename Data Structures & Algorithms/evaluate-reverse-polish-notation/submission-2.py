class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operands = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                secondTerm = int(stack.pop())
                firstTerm = int(stack.pop())

                if token == "+":
                    stack.append(firstTerm + secondTerm)
                elif token == "-":
                    stack.append(firstTerm - secondTerm)
                elif token == "*":
                    stack.append(firstTerm * secondTerm)
                elif token == "/":
                    stack.append(int(firstTerm / secondTerm))
        
        return stack[0]