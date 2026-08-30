class MinStack:
    def __init__(self):
        self.currMin = (2 ** 31) - 1
        self.stack = []

    def push(self, val: int) -> None:
        self.currMin = min(self.currMin, val)
        self.stack.append((val, self.currMin))

    def pop(self) -> None:
        self.stack.pop()
        self.currMin = self.stack[-1][1] if self.stack else (2 ** 31) - 1
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]