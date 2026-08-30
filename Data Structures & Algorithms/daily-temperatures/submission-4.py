class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            if stack and temp > stack[-1][1]:
                while stack and temp > stack[-1][1]:
                    res[stack[-1][0]] = idx - stack[-1][0]
                    stack.pop()
            stack.append((idx, temp))

        return res